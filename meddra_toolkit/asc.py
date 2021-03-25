import os

ASC_SEPARATOR = "$"
ASC_ENCODING = "iso8859-15"

def read_asc_file(file_path: str, columns: [str] = None, separator: str = ASC_SEPARATOR, encoding: str = ASC_ENCODING):
    with open(file_path, "r", encoding=encoding) as asc_file:
        line_count = 0
        for line in asc_file.readlines():
            line_count += 1
            cols = line.strip().split(separator)
            if not columns:
                yield cols
            else:
                if len(columns) != len(cols):
                    raise ValueError(f"Expecting {len(columns)} columns but got {len(cols)} columns at line {line_count} of file {file_path}")
                yield dict(zip(columns,cols))