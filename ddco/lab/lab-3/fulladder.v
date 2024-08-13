// module fulladder(os,oc,i2,i2,i3);
// 
// output os, oc;
// input i1, i2, i3;
// 
// wire t1,t2,t3,t4,t5;
// 
// xor(t1, i1, i2);
// xor(os, t1, i3);
// 
// and(t2, i1, i2);
// and(t3, i2, i3);
// and(t4, i3, i1);
// 
// or(t5, t2, t3);
// or(oc, t5, t4);
// 
// endmodule;
// 
// 
// This depends on lib.v
module fulladder(os,oc,i1,i2,i3);

output os, oc;
input i1, i2, i3;

wire t1,t2,t3;

halfadder ha1(t1,t2,i1,i2);
halfadder ha2(os,t3,t1,i3);
or(oc,t2,t3);

endmodule;
