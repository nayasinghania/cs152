// first function f1

module function1(x1, x2, x3, x4, y);
  input x1, x2, x3, x4;
  output y;

  wire a, b, c, d, e, f, g, h;

  and(a, x1, ~x3);
  and(b, x2, ~x3);
  and(c, ~x3, ~x4);
  and(d, x1, x2);
  and(e, x1, ~x4);

  or(f, a, b);
  or(g, c, d);
  or(h, e, g)  
  or(y, f, h;
endmodule

// second function f2

module function2(x1, x2, x3, x4, y);
  input x1, x2, x3, x4;
  output y;

  wire a, b, c, d, e, f;

  or(a, x1, ~x3);
  or(b, x1, x2);
  or(c, b, ~x4);
  or(d, x2, ~x3);
  or(e, d, ~x4);

  and(f, a, c);
  and(y, f, e);
endmodule