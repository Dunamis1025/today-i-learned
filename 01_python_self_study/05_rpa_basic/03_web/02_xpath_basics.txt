# 🌐 XPath Basics

XPath is used to select elements from HTML or XML documents.

It is widely used in:
- Web scraping
- Automation (Selenium)
- Data extraction

---

# 📌 1. What is XPath?

XPath allows you to locate elements based on:
- Structure
- Attributes
- Position

---

# 📌 2. Types of XPath

## 🔹 Absolute XPath

Starts from the root of the document.

Example:
/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/a

Problem:
- Very long
- Easily broken if structure changes

---

## 🔹 Relative XPath (Recommended)

Starts from anywhere using //

Example:
//*[@id="login"]

Advantage:
- Short
- More stable
- Easier to maintain

---

# 📌 3. Selecting by Attribute

Example:
//*[@student_id="1-1-5"]

Meaning:
Select element with attribute student_id = 1-1-5

---

# 📌 4. Selecting by Structure

Example:
//school/grade/class/student[2]

Meaning:
- Go to school
- Then grade
- Then class
- Select the 2nd student

---

# 📌 5. Sample XML Structure

<school name="Nado High School">
    <grade value="1st Grade">
        <class value="Class 1">
            <student number="1" student_id="1-1-1">Lee Jieun</student>
            <student number="2" student_id="1-1-2">Yoo Jaeseok</student>
            <student number="3" student_id="1-1-3">Cho Seho</student>
            <student number="4" student_id="1-1-4">Park Myungsoo</student>
            <student number="5" student_id="1-1-5">Lee Jieun</student>
        </class>
    </grade>
</school>

---

# 📌 6. Practical Examples (Real Web)

By ID:
//*[@id="account"]/div/a

Meaning:
Selects link inside account section

Login Button Example:
//*[@id="login"]

Meaning:
Finds login button using id

---

# 📌 7. Key Insight

XPath is powerful because:
- It can navigate complex structures
- It can filter using attributes
- It is essential for automation tools like Selenium

---

# 🔥 One-line Summary

XPath = Tool to locate elements using structure and attributes
