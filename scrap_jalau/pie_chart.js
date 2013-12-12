

var jsonData = {"Key" : "Apps" , "values" : [["application/java-archive","application/java-archive","application/java-archive","image/photoshop", "image/photoshop", "image/photoshop", "video/x-pn-realvideo", "audio/s3m"]]}

var values = jsonData.values[0];

var width = 960,
    height = 500,
    radius = Math.min(width, height) / 2;

var color = d3.scale.ordinal()
    .range(["#98abc5", "#12a123", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(radius - 70);

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d});

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var count = 0;

$(function(){
	var appDict = {},
		appCount = [];
		appNames = [];
		appNames2 = [];
		
	
	values.forEach(function(d){
		var app_type = d.split("/",1);
		appDict[app_type] = (appDict[app_type] || 0) + 1;
	});
	
	//Will create two arrays, one containing app names and the other
	//Containing the total counts.
	for(key in appDict){
		if(appDict.hasOwnProperty(key)){
			appNames.push(key);
			appNames2.push(key);
			appCount.push(appDict[key]);
			count = count + 1;
		}
	}
	appNames.reverse();
	appNames2.reverse();
	
	var g = svg.selectAll(".arc")
      .data(pie(appCount))
	  .enter().append("g")
      .attr("class", "arc");

	g.append("path")
      .attr("d", arc)
      .style("fill", function(key) { return color(appNames2.pop()); });

	g.append("text")
      .attr("transform", function(key) { return "translate(" + arc.centroid(key) + ")"; })
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
      .text(function(key) { return appNames.pop(); });

});