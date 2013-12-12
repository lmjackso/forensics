// Generate a log-normal distribution with a median of 30 minutes.
//var values = d3.range(1000).map(d3.random.logNormal(Math.log(30), .4));

Array.prototype.max = function() {
  return Math.max.apply(null, this);
};

Array.prototype.min = function() {
  return Math.min.apply(null, this);
};

// Simplifies the given json into an array we can work with.
var values = jsonData.values[0];
//[1, 5, 10, 3, 5, 8, 4, 12, 5, 4, 5, 6, 2, 3, 2, 5, 8, 9, 7, 10, 4, 2, 1, 10, 35, 40, 32, 36, 34, 23, 85, 81, 49, 30, 28, 58, 68, 39, 48, 1, 40]

// Formatters for counts and times (converting numbers to Dates).
var formatCount = d3.format(",.0f")
    // formatTime = d3.time.format("%H:%M"),
    // formatMinutes = function(d) { return formatTime(new Date(2012, 0, 1, 0, d)); };

var margin = {top: 10, right: 30, bottom: 30, left: 30},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    // used math.max to get the greatest value in the range of values
    .domain([0, Math.max.apply(null,values)])
    .range([0, width])
    //.range([0, width]);

// Generate a histogram using twenty uniformly-spaced bins.
var data = d3.layout.histogram()
    // number of ticks = number of intervals?
    .bins(x.ticks(20))
    (values);

var y = d3.scale.linear()
    .domain([0, d3.max(data, function(d) { return d.y; })])
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
  //  .tickFormat(formatMinutes);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var bar = svg.selectAll(".bar")
    .data(data)
  .enter().append("g")
    .attr("class", "bar")
    .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

bar.append("rect")
    .attr("x", 1)
    .attr("width", x(data[0].dx) - 1)
    .attr("height", function(d) { return height - y(d.y); });

bar.append("text")
    .attr("dy", ".75em")
    .attr("y", 6)
    .attr("x", x(data[0].dx) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return formatCount(d.y); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);