# *********************************
# ---------->Variables<------------
# *********************************
# Syntax ==> [Variable name] [Assignment operator] [Value]
# ---------------------------------
# Name convention & Rules
# [1] Name should start with [A-Z] or [a-z] or _
# [2] & can't start with NUM or Special characters (!, @, #, $, %, ^, &, *, -, =, +, <, ...)
# [3] BUT can include num & _
# [4] BUT can't include special characters (!, @, #, $, %, ^, &, *, -, =, +, <, ...)
# [5] Name is not like name [sensitive case]
# ---------------------------------
# How to write Variables?
name = "Ahmed Alaa" # one word => Normal
myName = "Ahmed Alaa" # two words => Camelcase
my_name = "Ahmed Alaa" # two words => snake_case
print(name)
print(myName)
print(my_name)
# ---------------------------------
# Source code: هو الكود اللي بنكتبه بنفسنا
# Transulation: هي الترجمه من الكلام اللي بنكتبه للغة الكمبيوتر
# Compilation: ترجمة الكود قبل run time
# Run time: هي المده التي يحتاجها البرنامج لتنفيذ الكود
# Interpreted: ترجمة الكود خلال تنفيذه
# ----------------------------------
# مقدرش اعمل متغير نفس اسم من الكلمات المحجوزه زي [if, class, True, etc..]
# الكلمات المحجوزه لما بكتبها بيكون ليها لون معين، اما الكلمات اللي اقدر استخدمها هتكون باللون الابيض
help("keywords") # الطريقه اللي اقدر اعرف بيها كل الكلمات المحجوزه في النظام
#----------------------------------
#How to write more than one Var.
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)