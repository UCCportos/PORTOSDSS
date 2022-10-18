
$.when( $.ready ).then(function() {
    const form_values_stored = sessionStorage.getItem("dss_form");
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    if(form_values_stored){
        const form_value = JSON.parse(form_values_stored);
        var elements = document.getElementById("dss_form").elements;
        document.getElementById("location").value = form_value.location;
        for (var i = 0, element; element = elements[i++];) {
           if(form_value[element.name]){
            element.value = form_value[element.name]
           }
           
        }
    }
   });

  function saveStorage(event){
    const formElement = sessionStorage.getItem("dss_form");
    const location_value = event.value;
    const inputName = event.name;
    const form = {...JSON.parse(formElement),[inputName]:location_value}; // looping through form challange is here due to key
    sessionStorage.setItem("dss_form",JSON.stringify(form))
  } 