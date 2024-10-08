module ld_3_8_tb;

wire i0,i1,i2,i3,i4,i5,i6,i7;
reg s0,s1,s2;

ld_3_8 ld(i0,i1,i2,i3,i4,i5,i6,i7,s2,s1,s0);

initial
begin
s2=0;s1=0;s0=0;
#100 s2=0;s1=0;s0=1;
#100 s2=0;s1=1;s0=0;
#100 s2=0;s1=1;s0=1;
#100 s2=1;s1=0;s0=0;
#100 s2=1;s1=0;s0=1;
#100 s2=1;s1=1;s0=0;
#100 s2=1;s1=1;s0=1;
end

initial
begin
$monitor($time,"-i0=%b,i1=%b,i2=%b,i3=%b,i4=%b,i5=%b,i6=%b,i7=%b, s2=%b,s1=%b,s0=%b",i0,i1,i2,i3,i4,i5,i6,i7,s2,s1,s0);
$dumpfile("./ld_3_8_tb.vcd");
$dumpvars(0,ld_3_8_tb);
end

endmodule;
