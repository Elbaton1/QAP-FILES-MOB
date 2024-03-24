const MotelCustomer = {
  Name: "Michael O'brien",
  BirthDate: "1998-05-15",
  Gender: "Male",
  RoomPreferences: ["Non-smoking", "King Bed"],
  PaymentMethod: "Debit card",
  MailingAddress: {
    Street: "541 Topsail Road",
    City: "St. John's",
    Province: "NL",
    PostalCode: "A1E 2B6",
    Country: "Canada",
  },
  PhoneNumber: "123-456-7890",
  CheckIn: "2024-03-22",
  CheckOut: "2024-03-26",

  calculateAge() {
    const birthDate = new Date(this.BirthDate);
    const currentDate = new Date();

    let age = currentDate.getFullYear() - birthDate.getFullYear();

    if (
      currentDate.getMonth() < birthDate.getMonth() ||
      (currentDate.getMonth() === birthDate.getMonth() &&
        currentDate.getDate() < birthDate.getDate())
    ) {
      age--;
    }

    return age;
  },

  calculateStayDuration() {
    const checkInDate = new Date(this.CheckIn);
    const checkOutDate = new Date(this.CheckOut);
    const durationInDays = (checkOutDate - checkInDate) / (24 * 60 * 60 * 1000);
    return Math.floor(durationInDays);
  },

  Description() {
    const age = this.calculateAge();
    const stayDuration = this.calculateStayDuration();

    return `
      <p>Name: ${this.Name}</p>
      <p>Age: ${age}</p>
      <p>Gender: ${this.Gender}</p>
      <p>Room Preferences: ${this.RoomPreferences.join(", ")}</p>
      <p>Payment Method: ${this.PaymentMethod}</p>
      <p>Mailing Address: ${this.MailingAddress.Street}, ${
      this.MailingAddress.City
    }, ${this.MailingAddress.Province}, ${this.MailingAddress.PostalCode}, ${
      this.MailingAddress.Country
    }</p>
      <p>Phone Number: ${this.PhoneNumber}</p>
      <p>Check-in Date: ${this.CheckIn}</p>
      <p>Check-out Date: ${this.CheckOut}</p>
      <p>Stay Duration: ${stayDuration} days</p>
    `;
  },
};

console.log(MotelCustomer.Description());
