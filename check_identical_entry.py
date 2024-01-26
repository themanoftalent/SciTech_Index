from glob import glob
from pathlib import Path


lls_all_entry = []

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_text = Path(s_file_path).read_text()
	ls_file_text_in_line = s_text.splitlines()
	for s_line in ls_file_text_in_line[1:]:
		if s_file_path.startswith('_') and s_line.endswith('\t'*2) or s_line.endswith('\t'*3):
			continue
		lls_all_entry.append([s_line, s_file_path])

lls_all_entry.sort()
s_concept_or_subject = lls_all_entry[0][0].split('\t')[1]
for i_entry_index in range(len(lls_all_entry)-1):
	s_next_concept_or_subject = lls_all_entry[i_entry_index+1][0].split('\t')[1]
	
	if s_concept_or_subject != '' and s_concept_or_subject == s_next_concept_or_subject:
		print(lls_all_entry[i_entry_index])
		print(lls_all_entry[i_entry_index+1])
	s_concept_or_subject = s_next_concept_or_subject
