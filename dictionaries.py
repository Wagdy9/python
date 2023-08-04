#Dictionaries
# the dictionaries by using the name followed by equal sign followed by curly braces then "":""



convert_month = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(convert_month["Jan"])
print(convert_month["Feb"])
print(convert_month.get("Jan"))
print(convert_month.get("Mar"))



print(convert_month.get("sthg", "The key can't be located"))



