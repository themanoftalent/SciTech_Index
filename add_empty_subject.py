from glob import glob
from pathlib import Path

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/*/**/', recursive=True):
	s_file_name = '_' + s_file_path[s_file_path.rstrip('/').rfind('/')+1:].rstrip('/') + '_.md'
	file_path = Path(s_file_path).joinpath(s_file_name)
	if not file_path.is_file():
		print(file_path)
		s_text = f'''| | |
|-|-|
| arb-Arab-ZZ |  |
| cmn-Hans-CN |  |
| cmn-Latn-CN |  |
| dan-Latn-DK |  |
| deu-Latn-DE |  |
| eng-Latn-US | {s_file_name.removesuffix('.md')} |
| fin-Latn-FI |  |
| fra-Latn-FR |  |
| heb-Hebr-IL |  |
| hin-Deva-IN |  |
| ita-Latn-IT |  |
| jpn-Hrkt-JP |  |
| jpn-Jpan-JP |  |
| kor-Hang-KR |  |
| kor-Kore-KR |  |
| nld-Latn-NL |  |
| nob-Latn-NO |  |
| pes-Aran-IR |  |
| por-Latn-PT |  |
| rus-Cyrl-RU |  |
| swe-Latn-SE |  |
| spa-Latn-ES |  |
| zxx-Zsym-ZZ |  |
|  |  |
'''
		file_path.write_text(s_text)
