$("#menu-toggle").click(function(e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});

$(".list-group-item").on('click', function(event) {
  event.preventDefault();

  console.log("Clicked: " + this.id);
  $.getJSON("/" + this.id, function(data) {
    //data is the JSON string
    console.log(data);
    simple_chart_config = {
      chart: {
          container: "#tree-simple"
      },

      nodeStructure: data
  };
  var my_chart = new Treant(simple_chart_config);


});

});
simple_chart_config = {
chart: {
    container: "#tree-simple"
},

nodeStructure: {
    text: { name: "Parent node" },
    children: [
        {
            text: { name: "First child" }
        },
        {
            text: { name: "Second child" }
        }
    ]
}
};

var my_chart = new Treant(simple_chart_config);