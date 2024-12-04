function updateMemberInfo() {
      const select = document.getElementById("update-member-select");
      const selectedOption = select.options[select.selectedIndex];

      const lastNameInput = document.getElementById("last-name");
      const firstNameInput = document.getElementById("first-name");
      const dateOfBirthInput = document.getElementById("date-of-birth");
      const placeOfBirthInput = document.getElementById("place-of-birth");
      const cityOfResidenceInput = document.getElementById("city-of-residence");
      const phoneNumberInput = document.getElementById("phone-number");
      const emailInput = document.getElementById("e-mail");
      const memberIdInput = document.getElementById("member-id");

      lastNameInput.value = selectedOption.getAttribute("data-last-name") || "";
      firstNameInput.value = selectedOption.getAttribute("data-first-name") || "";
      dateOfBirthInput.value = selectedOption.getAttribute("data-date-of-birth") || "";
      placeOfBirthInput.value = selectedOption.getAttribute("data-place-of-birth") || "";
      cityOfResidenceInput.value = selectedOption.getAttribute("data-city-of-residence") || "";
      phoneNumberInput.value = selectedOption.getAttribute("data-phone-number") || "";
      emailInput.value = selectedOption.getAttribute("data-email") || "";
      memberIdInput.value = selectedOption.getAttribute("value") || "";
}