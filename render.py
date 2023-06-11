import tomllib
import pandas as pd

if __name__ == '__main__':

    table = []

    with open("projects.toml", "rb") as f:
        projects = tomllib.load(f)

        for key, project in projects.items():
            org = project.get("org", "J535D165")

            record = {
                "url": f"[{org}/{key}](https://github.com/{org}/{key})"
            }

            record["license"] = f"![GitHub License](https://img.shields.io/github/license/{org}/{key})"
            record["stars"] = f"![GitHub Repo stars](https://img.shields.io/github/stars/{org}/{key})"


            pypi_name = project.get("pypi_name", key)
            if project.get("pypi", False):
                record["download_total"] = f"[![Downloads](https://static.pepy.tech/personalized-badge/{pypi_name}?period=total&units=international_system&left_color=black&right_color=yellow&left_text=Downloads)](https://pepy.tech/project/{pypi_name})"
                record["download_month"] = f"[![Downloads](https://static.pepy.tech/personalized-badge/{pypi_name}?period=month&units=international_system&left_color=black&right_color=yellow&left_text=Downloads)](https://pepy.tech/project/{pypi_name})"

            table.append(record)
    df = pd.DataFrame(table).fillna("")
    print(df)

    with open("PROJECTS.md", "w") as f:
        f.write(df.to_markdown())
