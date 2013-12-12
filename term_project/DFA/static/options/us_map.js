//var types = [['latitude', 'longitude']];
var values = jsonData[0].values;

var width = 960,
    height = 500;

var projection = d3.geo.albersUsa()
    .scale(1070)
    .translate([width / 2, height / 2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select(".chart").insert("svg:svg", "h2")
    .attr("width", width)
    .attr("height", height);
	
var g = svg.append("g")

	
var circles = svg.append("svg:g")
    .attr("id", "circles");
	
g.append("rect")
    .attr("class", "background")
    .attr("width", width)
    .attr("height", height);

	
d3.json("uss.json", function(error, us) {
	g.append("g")
		.attr("class", "subunit")
	.selectAll("path")
		.data(topojson.feature(us, us.objects.subunits4).features)
    .enter().append("path")
      .attr("d", path);

});

$(function() {
	for(x in values){
		//points[0] is latitude and points[1] is longitude
		try{
		var location = [+values[x][1], +values[x][0]];
		//positions.push(projection(location));
		svg.append("circle").attr("id", "circles").attr("r",10).attr("transform", function() {return "translate(" + projection(location) + ")";});
		}
		catch(err){
		alert("You must only submit location data to this chart!")
		}	
	}
});
