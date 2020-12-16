// need jquery

function goPython(){
  console.log("working...");

  var x = document.getElementById("loading");
  x.style.display = "block";

  // var newFolderName="wordcloud";
  // var newFolderNode=parentFolderNode.childByNamePath(newFolderName);

  // var passed_time = 0

  // while (newFolderNode === null) {
  //   passed_time = passed_time+1
  // }

  // x.style.display = "none";

  // window.location.reload()

};

// <script type="text/javascript">
//             $(document).ready(function() {
//                 if ($("result_wordcloud").is("[src]")) {
//                     $("result_wordcloud").removeAttr("src");
//                 }
//                 // $("#result_wordcloud").attr('src', '{{url_for('static', filename='wordcloud.png')}}');
//                 $.ajax({ 
//                     medthod: 'POST',
//                     url:'/result',
//                     success: function(data){
//                         $("#result_wordcloud").attr('src', '{{url_for('static', filename='wordcloud.png')}}');
//             })
        
//             // $("#result_wordcloud").change(function(){
//             //     var sliderVal = $(this).val();
//             //     $.ajax({ 
//             //         medthod: 'POST',
//             //         url:'/imgp/nr/',
//             //         data: JSON.stringify({slider: sliderVal}),
//             //         success: function(data){
//             //             $("#result_wordcloud").attr('src', 'data:image/png;base64, ' + data);
//             //         }
//             //     });
//             // });
//             </script>
        



