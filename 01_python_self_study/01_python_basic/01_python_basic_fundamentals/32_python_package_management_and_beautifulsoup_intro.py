"""
📌 What I learned: Python package management and installing BeautifulSoup

In this lesson, I learned how to manage external Python packages using pip
and how to install, inspect, and verify the BeautifulSoup library
through hands-on practice in the terminal.

1. Understanding Python modules and file locations
--------------------------------------------------
I used the inspect module to check the actual file path of a Python standard library.

Example:
    import inspect
    import random
    print(inspect.getfile(random))

This showed me where Python modules are physically stored on my system,
helping me understand how Python loads and manages modules internally.


2. What pip and PyPI are (and why it is called pip)
--------------------------------------------------
- PyPI (Python Package Index) is an online repository where developers share Python packages.
- pip is the command-line tool used to install and manage those packages.

pip originally stood for:
    "Pip Installs Packages"
(or historically, "Preferred Installer Program")

That is why we type `pip` instead of `pyp`.
pip is simply the installer tool, while PyPI is the package repository.


3. Installing BeautifulSoup with pip
------------------------------------
I installed BeautifulSoup using the following command:

    pip install beautifulsoup4

Terminal output example:
    Requirement already satisfied: beautifulsoup4
    Requirement already satisfied: soupsieve
    Requirement already satisfied: typing-extensions

This confirmed that the package and its dependencies
were successfully installed in my virtual environment.


4. Verifying installation with a simple HTML example
----------------------------------------------------
I tested whether BeautifulSoup was working correctly by parsing a small HTML snippet:

    from bs4 import BeautifulSoup
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())

Output:
    <p>
     Some
     <b>
      bad
      <i>
       HTML
      </i>
     </b>
    </p>

This demonstrated that BeautifulSoup automatically fixes
and organizes broken or incomplete HTML structures.


5. Inspecting installed packages
--------------------------------
I used the following pip commands to inspect my environment:

    pip list
    pip show beautifulsoup4

These commands allowed me to:
- See which packages are installed
- Check the installed version
- Confirm the installation location inside the virtual environment


6. Upgrading and uninstalling packages
--------------------------------------
I also learned how to maintain packages:

    pip install --upgrade beautifulsoup4
    pip uninstall beautifulsoup4

This helped me understand that external libraries
can be easily updated or removed when they are no longer needed.


7. Why this lesson matters
--------------------------
At this stage, the focus was not on web scraping logic itself,
but on learning how and when to prepare external libraries properly.

This lesson serves as a foundational step before learning:
- Web scraping with requests + BeautifulSoup
- Data extraction and automation
- Real-world Python projects that depend on external libraries
"""
