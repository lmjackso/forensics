//var data = jsonData.values[0];
var data =[4, 8, 15, 16, 23, 42];
//var types = ['last_modification', 'mime_type', 'file_size'];
//var data = jsonData[0].values

alert('you are here')
alert(data)

var x = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, 420]);

d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return x(d) + "px"; })
    .text(function(d) { return d; });

