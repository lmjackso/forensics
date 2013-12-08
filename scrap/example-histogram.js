 

Discover Gists
patjang92
 
 
Star 12
 
Fork 10
PUBLIC
 rduplain / responsive_d3_example.html
Last active 19 days ago — forked from mattalcock/responsive_d3_example.html

Responsive d3.js D3 Javascript Histogram Example
Gist Detail
Revisions 2
Stars 12
Forks 10
Download Gist
Clone this gist

Embed this gist

Link to this gist

responsive_d3_example.htmlHTML
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
<!DOCTYPE html>
<script src="http://mbostock.github.com/d3/d3.v2.js?2.8.1"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<style>
 
body {
  font: 10px sans-serif;
}
 
rect {
  fill: steelblue;
  stroke: white;
}
 
line {
  stroke: black;
  shape-rendering: crispEdges;
}
 
</style> 
<body> 
 
<div class='histogram' style="width:50%" >
</div>
 
</body> 
<script> 
 
// Generate an Irwin-Hall distribution.
function gen_ih_dist(trails, variables)
{
  data = [];
 
  for (var i = 0; i < trails; i++) {
    for (var s = 0, j = 0; j < variables; j++) {
      s += Math.random();
    }
    data.push(s);
  }
  return data;
}
 
var div_name = "div.histogram";
 
pos_data = gen_ih_dist(1000, 10);
neg_data = gen_ih_dist(1000, 10);
 
draw_histogram(div_name, pos_data, neg_data);
 
//The drawing of the histogram has been broken out from the data retrial 
// or computation. (In this case the 'Irwin-Hall distribution' computation above)
 
function draw_histogram(reference, pos_data, neg_data){
 
$(reference).empty()
 
//The drawing code needs to reference a responsive elements dimneions
var width = $(reference).width();
// var width = $(reference).empty().width(); we can chain for effeicanecy as jquery returns jquery.
 
var height = 250;  // We don't want the height to be responsive.
 
var histogram = d3.layout.histogram() (pos_data);
var neg_histogram = d3.layout.histogram()(neg_data);
 
var x = d3.scale.ordinal()
    .domain(histogram.map(function(d) { return d.x; }))
    .rangeRoundBands([0, width]);
 
var y = d3.scale.linear()
    .domain([0, d3.max(histogram.map(function(d) { return d.y; }))])
    .range([0, height]);
 
var ny = d3.scale.linear()
    .domain([0, d3.max(neg_histogram.map(function(d) { return d.y; }))])
    .range([0, height]);
 
var svg = d3.select(reference).append("svg")
    .attr("width", width)
    .attr("height", 2 * height);
 
svg.selectAll("rect")
    .data(histogram)
  .enter().append("rect")
    .attr("width", x.rangeBand())
    .attr("x", function(d) { return x(d.x); })
    .attr("y", function(d) { return height - y(d.y); })
    .attr("height", function(d) { return y(d.y); });
 
svg.selectAll("rect-neg")
    .data(neg_histogram)
  .enter().append("rect")
    .style("fill", "red")
    .attr("width", x.rangeBand())
    .attr("x", function(d) { return x(d.x); })
    .attr("y", function(d) { return height})
    .attr("height", function(d) { return ny(d.y); });
 
svg.append("line")
    .attr("x1", 0)
    .attr("x2", width)
    .attr("y1", height)
    .attr("y2", height);
  
};
 
//Bind the window resize to the draw method.
//A simple bind example is
 
//$(window).resize(function() {
//  draw_histogram(div_name, pos_data, neg_data);
//});
 
//A better idom for binding with resize is to debounce
var debounce = function(fn, timeout) 
{
  var timeoutID = -1;
  return function() {
    if (timeoutID > -1) {
      window.clearTimeout(timeoutID);
    }
    timeoutID = window.setTimeout(fn, timeout);
  }
};
 
var debounced_draw = debounce(function() {
  draw_histogram(div_name, pos_data, neg_data);
}, 125);
 
$(window).resize(debounced_draw);
 
</script> 

 afedulov commented 5 months ago
This example helped me a LOT! Thanks for sharing!

 amytych commented 2 months ago
Same here, thanks for this gist, helped me a lot!

Write Preview Comments are parsed with GitHub Flavored Markdown

Add Comment
© 2013 GitHub Inc. All rights reserved.
The GitHub Blog Support Contact