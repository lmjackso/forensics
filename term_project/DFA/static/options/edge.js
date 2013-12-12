// http://blog.thomsonreuters.com/index.php/mobile-patent-suits-graphic-of-the-day/


var values = jsonData[0].values;
//var types = [['last_modification', 'file_name']];
//var values = [["2003-06-16 07:57:23.235000","asdf"],["2003-06-16 07:57:28.235000", "fdsa"],["2003-06-16 07:57:20.235000", "qwer"],["2003-06-16 07:56:23.235000", "trewq"],["2004-06-16 07:57:23.235000", "tree"],["2004-06-16 07:57:13.235000", "poiu"],["2004-06-16 07:57:25.235000", "lkhj"],["2003-06-16 08:57:23.235000", "mbnv"],["2003-06-16 06:57:23.235000", "bnm"]];
var links = [];
var tempDict = {};
var difference = 10000;

values.forEach(function(file1){
	values.forEach(function(file2)
	{
	if(file1[1] == file2[1]){ }
	else{
		var time1 = Date.parse(file1[0]).valueOf();
		var time2 = Date.parse(file2[0]).valueOf();
		//alert(time1);
		//alert(time2);
		if(Math.abs(time1 - time2) <  difference){
			tempDict = {"source" : file1[1], "target" : file2[1], "type" : "suit"};
			alert(tempDict);
			links.push(tempDict);
		}
		
	}
	});
});

var nodes = {};

// Compute the distinct nodes from the links.
links.forEach(function(link) {
  link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
  link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
});

var width = 960,
    height = 500;

var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([width, height])
    .linkDistance(60)
    .charge(-300)
    .on("tick", tick)
    .start();

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

// Per-type markers, as they don't inherit styles.
svg.append("defs").selectAll("marker")
    .data(["suit", "licensing", "resolved"])
  .enter().append("marker")
    .attr("id", function(d) { return d; })
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
  .append("path")
    .attr("d", "M0,-5L10,0L0,5");

var path = svg.append("g").selectAll("path")
    .data(force.links())
  .enter().append("path")
    .attr("class", function(d) { return "link " + d.type; })
    .attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

var circle = svg.append("g").selectAll("circle")
    .data(force.nodes())
  .enter().append("circle")
    .attr("r", 6)
    .call(force.drag);

var text = svg.append("g").selectAll("text")
    .data(force.nodes())
  .enter().append("text")
    .attr("x", 8)
    .attr("y", ".31em")
    .text(function(d) { return d.name; });

// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
  path.attr("d", linkArc);
  circle.attr("transform", transform);
  text.attr("transform", transform);
}

function linkArc(d) {
  var dx = d.target.x - d.source.x,
      dy = d.target.y - d.source.y,
      dr = Math.sqrt(dx * dx + dy * dy);
  return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
}

function transform(d) {
  return "translate(" + d.x + "," + d.y + ")";
}