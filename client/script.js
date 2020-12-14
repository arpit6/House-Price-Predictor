function getUnderValue() {
  // Get Under Construction
  var uiUNDC = document.getElementsByName("uiUNDC");
  for (var i in uiUNDC) {
    if (uiUNDC[i].checked) {
      return parseInt(i);
    }
  }
  return 0; // Invalid Value
}

function getPostedValue() {
  // Get Posted By
  var uiPOST = document.getElementsByName("uiPOST");
  for (var i in uiPOST) {
    if (uiPOST[i].checked) {
      return parseInt(i);
    }
  }
  return 0; // Invalid Value
}

function getReraValue() {
  // Get Real State Authorised
  var uiRERA = document.getElementsByName("uiRERA");
  for (var i in uiRERA) {
    if (uiRERA[i].checked) {
      return parseInt(i);
    }
  }
  return 0; // Invalid Value
}


function onClickedEstimatePrice() {
  console.log("Estimated Price button clicked");
  var sqft = document.getElementById("uiSqft");
  var undc = getUnderValue();
  var post = getPostedValue();
  var bhk = document.getElementById("uiBHK");
  var location = document.getElementById("uiLocations");
  var rera = getReraValue();
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";
//     var url = "/api/predict_home_price"; // only Deployment

  $.post(
    url,
    {
      city : location.value,
      POSTED_BY : post,
      UNDER_CONSTRUCTION : undc,
      RERA : rera,
      BHK_NO : parseFloat(bhk.value),
      SQUARE_FT : parseFloat(sqft.value)
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
    });

}

function onPageLoad() {
    console.log("document loaded");
  var url = " http://127.0.0.1:5000/get_location_names";
//     var url = "/api/get_location_names"; // only Deployment
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    // function to render the location names
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]); // Add location to drop drown list
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
