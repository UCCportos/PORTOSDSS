
$.when( $.ready ).then(function() {
    console.log(document.getElementById("location"));
    const form_values_stored = sessionStorage.getItem("dss_form");
    if(form_values_stored){
        const form_value = JSON.parse(form_values_stored);
        var elements = document.getElementById("dss_form").elements;
        document.getElementById("location").value = form_value.location;
        for (var i = 0, element; element = elements[i++];) {
           if(form_value[element.name]){
            element.value = form_value[element.name]
           }else{
            element.value = 0;
           }
           
        }
    }
   });

  function saveStorage(event){
    console.log('Save storage',event.name)
    const formElement = sessionStorage.getItem("dss_form");
    const location_value = event.value;
    const inputName = event.name;
    const form = {...JSON.parse(formElement),[inputName]:location_value}; // looping through form challange is here due to key
    sessionStorage.setItem("dss_form",JSON.stringify(form))
    console.log('Save storage',sessionStorage.getItem("dss_form"))
  } 