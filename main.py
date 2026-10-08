from pyscript import document, display


# ICT Tech Club directory. Checks case-insensitive.
MEMBER_NAMES = {
    "christopher francis p. de vera": "Christopher Francis P. De Vera",
    "jan immanuel d. cabading": "Jan Immanuel D. Cabading",
    "carlos eziquel b. borromeo": "Carlos Eziquel B. Borromeo",
    "jericho t. magsalin": "Jericho T. Magsalin",
    "louie vonn m. lee": "Louie Vonn M. Lee",
    "gerthy b. bausa": "Gerthy B. Bausa",
}

#lookup process
def lookup_confirm(e):
    if e:
        e.preventDefault()

    member_name = " ".join(document.getElementById("name-input").value.split())
    result_box = document.getElementById("result")
    result_target = document.getElementById("result-content")

    # Reset display state before showing the new result.
    result_box.classList.add("active")
    result_box.classList.remove("not-member")

    # Check if the input is empty.
    if not member_name:
        result_box.classList.add("not-member")
        display("Enter a member name to run the directory check.", target=result_target, append=False)
        return

    member = MEMBER_NAMES.get(member_name.casefold())
    if member:
        message = f"MEMBER VERIFIED {member} is an ICT Club member."
    else:
        result_box.classList.add("not-member")
        message = f"NO MATCH {member_name} is not listed in the ICT Club directory."

    display(message, target=result_target, append=False)


