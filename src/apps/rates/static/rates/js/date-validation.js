
document.addEventListener('DOMContentLoaded', () => {
    
    const startDate = document.getElementById('id_start_date')
    const endDate = document.getElementById('id_end_date')

  function validateDates() {
    const today = new Date().toISOString().split('T')[0];

    let message = ""; 

    if (startDate.value > today || endDate.value > today) {
      message = "The period must not be after today!";
    } else if (startDate.value > endDate.value) {
      message = "End date must be after start date!";
    }

    if (message) 
      return showMessage(message, "warning");
   
    hideMessage();
    
  };

startDate.addEventListener('change', validateDates);
endDate.addEventListener('change', validateDates);

})