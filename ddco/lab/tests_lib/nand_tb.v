module nand_tb;

reg i1, i2;
wire o;

nand2 nand2_inst(o, i1, i2);

initial
begin
$display("Testbench for NAND gate");
i1=0; i2 = 0;
#10 i1=0; i2 = 1;
#10 i1=1; i2 = 0;
#10 i1=1; i2 = 1;
end

initial
begin
$monitor($time, " - i1 = %b, i2 = %b, o= %b", i1, i2, o);
end

endmodule;
