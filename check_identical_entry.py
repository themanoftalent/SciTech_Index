from glob import glob
from pathlib import Path

lls_entry = []

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.md', recursive=True):
	s_text = Path(s_file_path).read_text()
	ls_text_line = s_text.splitlines()
	for s_line in ls_text_line[2:-1]:
		if s_file_path.endswith('_.md') and s_line.endswith(' |  |') or s_line.endswith(' |  |  |'):
			continue
		lls_entry.append([s_line, s_file_path])
for i_entry_index in range(len(lls_entry)):
	for ls_entry_to_check in lls_entry[i_entry_index+1:]:
		if ls_entry_to_check[0] == lls_entry[i_entry_index][0]:
			print(ls_entry_to_check[0])
			print(ls_entry_to_check[1])
			print(lls_entry[i_entry_index][1])
