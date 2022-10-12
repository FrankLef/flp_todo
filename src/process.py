import sys
from pathlib import Path

import pyarrow.feather as feather

import process.etl as etl

project_path = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_path))
from config import settings  # noqa

cfg = settings.msaccess
print(cfg.path)


# out = etl.build_engine(cfg.path)
# print(type(out))

out = etl.main(path=cfg.path, tables=cfg.tables)
# print(type(out))
# for key, value in out.items():
#     fn = Path(project_path).joinpath("data", f'{key}.feather')
#     feather.write_feather(value, fn)

# print(tuple(out)[0])
# {print(key) for key in out.keys()}

fn = Path(project_path).joinpath("data", f"{tuple(out)[0]}.feather")
df = feather.read_feather(fn)
print(df.info())
