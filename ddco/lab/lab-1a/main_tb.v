module and2_test;

reg a, b;
wire c;
and and2_test(c, a, b);

initial
begin
#000 a=0; b=0;
#100 a=0; b=1;
#100 a=1; b=0;
#100 a=1; b=1;
end

initial
begin
$monitor($time, "a=%b, b=%b, c=%b", a, b, c);
end

initial
begin
$dumpfile("and2_test.vcd"); //vcd - value change dump
$dumpvars(0, and2_test);
end
endmodule
