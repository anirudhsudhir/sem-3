module not_tb;

reg i1, i2;
wire o;

not2 not2_inst(o, i1);

initial
begin
$display("Testbench for NOT gate");
i1=0; i2 = 0;
#10 i1=0;
#10 i1=1;
end

initial
begin
$monitor($time, " - i1 = %b, o= %b", i1, o);
end

endmodule;
