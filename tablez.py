from prettytable import PrettyTable
mt = PrettyTable()
mt.field_names = ["Title", "Type", "Platform", "CVE"]
mt.add_row(["Apache Tomcat", "XXS", "Multiple", "2019-0221"])
mt.add_row(["Docker - Container Escape", "Local", "Linux", "N/A"])

print(mt)
