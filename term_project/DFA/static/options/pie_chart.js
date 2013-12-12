
//test jsonData
//var jsonData = {"Key" : "Apps" , "values" : [["application/java-archive","application/java-archive","application/java-archive","image/photoshop", "image/photoshop", "image/photoshop", "video/x-pn-realvideo", "audio/s3m"]]}

var values = jsonData[0].values;
var types = ['creation_date', 'mime_type', 'file_size'];
var width = 960,
    height = 500,
    radius = Math.min(width, height) / 2;

var color = d3.scale.ordinal()
    .range(["#d11141", "#00b159", "#00aedb", "#f37735", "#ffc425"]);

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
		app_type = "";
		
	
	values.forEach(function(d){
		try{
			app_type = d.split("/",1);
			}
		catch(err){
			app_type = d;
			}
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