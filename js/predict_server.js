$(function() {

  // preventing page from redirecting
  $("html").on("dragover", function(e) {
    e.preventDefault();
    e.stopPropagation();
    $("h1").text("Drag here");
});

$("html").on("drop", function(e) { e.preventDefault(); e.stopPropagation(); });

// Drag enter
$('.upload-area').on('dragenter', function (e) {
    e.stopPropagation();
    e.preventDefault();
    $("h1").text("Drop");
});

// Drag over
$('.upload-area').on('dragover', function (e) {
    e.stopPropagation();
    e.preventDefault();
    $("h1").text("Drop");
});

// Drop
$('.upload-area').on('drop', function (e) {
    e.stopPropagation();
    e.preventDefault();

    $("h1").text("Upload");

    var file = e.originalEvent.dataTransfer.files;
    var fd = new FormData();

    fd.append('file', file[0]);

    // uploadData(fd);
});

// Open file selector on div click
$("#uploadfile").click(function(){
    $("#file").click();
});

  // file selected
  $("#file").change(function () {
    var fd = new FormData();

    var files = $('#file')[0].files[0];

    var reader = new FileReader();

      reader.onload = function () {
        var image = new Image();
        image.src = reader.result;

    image.onload = function() {
        console.log(image.width);
        console.log(image.height);
        var max_height = 200;
        var max_width = 200;

        var new_height = image.height;
        var new_width = image.width;

        if((image.height >= image.width) && (image.height > max_height)){
          new_height = max_height;
          new_width = new_height*(image.width/image.height);
        }
        if(image.width >= image.height && image.width > max_width){
          new_width = max_width;
          new_height = new_width*(image.height/image.width);
        }

        console.log('new_height ' + new_height);
        console.log('new_width ' + new_width);
        $('#imgPreview')
          .attr('src', image.src)
          .width(new_width)
          .height(new_height);
    };
        
      };

      reader.readAsDataURL(files);

    fd.append('file', files);

    // uploadData(fd);
    console.log(files)
    // addThumbnail(files)
  });

  $("#predictForm input,#predictForm textarea").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var name = $("input#name").val();
      var email = $("input#email").val();
      var phone = $("input#phone").val();
      var message = $("textarea#message").val();
      var firstName = name; // For Success/Failure Message
      $("#output_text").text("Hello " + firstName + "!");
      // Check for white space in name for Success/Fail message
      if (firstName.indexOf(' ') >= 0) {
        firstName = name.split(' ').slice(0, -1).join(' ');
      }
      $this = $("#sendMessageButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "http://127.0.0.1:5002/json",
        type: "POST",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ 
          "device":"TempSensor", 
          "value":"270", 
          "timestamp":"25/01/2017 10:10:05" 
        }),
/*         {
          name: name,
          phone: phone,
          email: email,
          message: message
        }, */
        cache: false,
        success: function( data, textStatus, xhr ) {
          // Success message
          $('#success').html("<div class='alert alert-success'>");
          $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-success')
            .append("<strong>Your message has been sent. </strong>");
          $('#success > .alert-success')
            .append("Data: " + data);
          $('#success > .alert-success')
            .append('</div>');
          //clear all fields
          $('#predictForm').trigger("reset");
        },
        error: function( textStatus, xhr) {
          // Fail message
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-danger').append("Data: " + xhr.status);
          $('#success > .alert-danger').append($("<strong>").text("Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!"));
          $('#success > .alert-danger').append('</div>');
          //clear all fields
          $('#predictForm').trigger("reset");
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
  $('#success').html('');
});

// Added thumbnail
function addThumbnail(data){
  $("#uploadfile h1").remove(); 
  var len = $("#uploadfile div.thumbnail").length;

  var num = Number(len);
  num = num + 1;

  var name = data.name;
  var size = convertSize(data.size);
  var src = data.src;

  // Creating an thumbnail
  $("#uploadfile").append('<div id="thumbnail_'+num+'" class="thumbnail"></div>');
  $("#thumbnail_"+num).append('<img src="'+src+'" width="100%" height="78%">');
  $("#thumbnail_"+num).append('<span class="size">'+size+'<span>');

}

// Bytes conversion
function convertSize(size) {
  var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  if (size == 0) return '0 Byte';
  var i = parseInt(Math.floor(Math.log(size) / Math.log(1024)));
  return Math.round(size / Math.pow(1024, i), 2) + ' ' + sizes[i];
}