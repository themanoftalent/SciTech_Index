from glob import glob
from pathlib import Path


top_path = Path.cwd()

def check(s_sort_item, s_item_separator):
	s_tabbed_sort_item = s_sort_item.replace(s_item_separator, '\t').replace('\t'*2, s_item_separator*2)
	ls_concept_or_subject = s_tabbed_sort_item.split('\t')
	for i_item_index in range(len(ls_concept_or_subject)):
		ls_concept_or_subject[i_item_index] = ls_concept_or_subject[i_item_index].strip()
	if ls_concept_or_subject != sorted(ls_concept_or_subject):
		print(s_file_path)
		print(s_locale)
		print(sorted(ls_concept_or_subject))
		print()

def s_get_item_separator(s_writing_system, s_punctuation_type):
	if s_punctuation_type == 'comma':
		if s_writing_system in ['Arab', 'Aran']:
			return '،'
		elif s_writing_system == 'Bamu':
			return '꛵'
		elif s_writing_system in ['Bopo', 'Hrkt']:
			if len(ls_entry) == 2:
				s_sort_item = s_subject
			else:
				s_sort_item = s_concept + s_prerequisite
			if '，' in s_sort_item:
				return '，'
			else:
				return '、'
		elif s_writing_system == 'Ethi':
			return '፣'
		elif s_writing_system == 'Hmng':
			return '𖬹'
		elif s_writing_system == 'Lisu':
			return '꓾'
		elif s_writing_system == 'Medf':
			return '𖺗'
		elif s_writing_system == 'Mong':
			if len(ls_entry) == 2:
				s_sort_item = s_subject
			else:
				s_sort_item = s_concept + s_prerequisite
			if '᠈' in s_sort_item:
				return '᠈'
			else:
				return '᠂'
		elif s_writing_system == 'Newa':
			return '𑑍'
		elif s_writing_system == 'Nkoo':
			return '߸'
		elif s_writing_system == 'Sgnw':
			return '𝪇'
		elif s_writing_system == 'Tibt':
			return '༔'
		elif s_writing_system == 'Vaii':
			return '꘍'
		else:
			return ','
	elif s_punctuation_type == 'semicolon':
		if s_writing_system in ['Arab', 'Aran']:
			if len(ls_entry) == 2:
				s_sort_item = s_subject
			else:
				s_sort_item = s_concept + s_prerequisite
			if '⁏' in s_sort_item:
				return '⁏'
			else:
				return '؛'
		elif s_writing_system == 'Armn':
			return '․'
		elif s_writing_system == 'Bamu':
			return '꛶'
		elif s_writing_system in ['Bopo', 'Hani', 'Hans', 'Hant', 'Jpan']:
			return '；'
		elif s_writing_system == 'Grek':
			return '·'
		elif s_writing_system == 'Ethi':
			return '፤'
		elif s_writing_system == 'Sgnw':
			return '𝪉'
		else:
			return ';'

for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_text = Path(s_file_path).read_text()
	ls_file_text_in_line = s_text.splitlines()
	ls_file_text_in_line.pop(0)

	s_result_text = ls_file_text_in_line[0] + '\n' + ls_file_text_in_line[1] + '\n'
	for s_line in ls_file_text_in_line:
		ls_entry = s_line.split('\t')
		if len(ls_entry) == 2:
			s_locale, s_subject = ls_entry
		else:
			print(ls_entry)
			s_locale, s_concept, s_prerequisite = ls_entry

		s_language, s_writing_system, s_region = s_locale.split('-')
		if s_writing_system in ['Hani', 'Hans', 'Hant', 'Jpan', 'Kore']:
			continue

		if len(ls_entry) == 2:
			if s_subject != '':
				s_item_separator = s_get_item_separator(s_writing_system, 'comma')
				check(s_subject, s_item_separator)
		else:
			if s_concept != '':
				s_item_separator = s_get_item_separator(s_writing_system, 'comma')
				check(s_concept, s_item_separator)
			if s_prerequisite != '':
				s_item_separator = s_get_item_separator(s_writing_system, 'semicolon')
				check(s_prerequisite, s_item_separator)
