var margin = {top: 40, right: 20, bottom: 30, left: 40},
width = 960 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

var formatPercent = d3.format("d"); 

var x = d3.scale.ordinal()
	.rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
	.range([height, 0]);

var xAxis = d3.svg.axis()
	.scale(x)
	.orient("bottom");

var yAxis = d3.svg.axis()
	.scale(y)
	.orient("left")
	.tickFormat(formatPercent);

var tip = d3.tip()
	.attr('class', 'd3-tip')
	.offset([-10, 0])
	.html(function(d) {
	return "<strong>Promedio:</strong> <span style='color: #fff2b2'>" + d.Promedio + "</span>";
})

var svg = d3.select("body").append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);

d3.csv("datos/bar-data.csv", type, function(error, data) {

	data.forEach(function(d) {
	d.Promedio = +d.Promedio;
	});

	x.domain(data.map(function(d) { return d.Categoria; }));
	y.domain([0, d3.max(data, function(d) { return d.Promedio; })]);

	svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis);

	svg.append("g")
		.attr("class", "y axis")
		.call(yAxis)
		.append("text")
		.attr("transform", "rotate(-90)")
		.attr("y", 6)
		.attr("dy", ".71em")
		.style("text-anchor", "end")
		.text("Promedio");

	svg.selectAll(".bar")
		.data(data)
		.enter().append("rect")
		.attr("class", "bar")
		.attr("x", function(d) { return x(d.Categoria); })
		.attr("width", x.rangeBand())
		.attr("y", function(d) { return y(d.Promedio); })
		.attr("height", function(d) { return height - y(d.Promedio); })
		.on('mouseover', tip.show)
		.on('mouseout', tip.hide)
	
	d3.select("input").on("change", change);

	var sortTimeout = setTimeout(function() {
		d3.select("input").property("checked", true).each(change);
	}, 2000);

	function change() {
	clearTimeout(sortTimeout);

	// Copy-on-write since tweens are evaluated after a delay.
	var x0 = x.domain(data.sort(this.checked
		? function(a, b) { return b.Promedio - a.Promedio; }
		: function(a, b) { return d3.ascending(a.Categoria, b.Categoria); })
		.map(function(d) { return d.Categoria; }))
		.copy();

	svg.selectAll(".bar")
		.sort(function(a, b) { return x0(a.Categoria) - x0(b.Categoria); });

	var transition = svg.transition().duration(750),
		delay = function(d, i) { return i * 50; };

	transition.selectAll(".bar")
		.delay(delay)
		.attr("x", function(d) { return x0(d.Categoria); });

	transition.select(".x.axis")
		.call(xAxis)
		.selectAll("g")
		.delay(delay);
	}

});

function type(d) {
	d.Promedio = +d.Promedio;
	return d;
}