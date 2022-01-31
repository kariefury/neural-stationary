// Design
// D flip-flop
module fiveclocks (clk,b,reset,t,tt,ttt,tttt,ttttt,m);
  input      clk;
  input      b;
  input		 reset;
  output     t,tt,ttt,tttt,ttttt,m;

  reg        the,thethe,thethethe,thethethethe,thethethethethe;
  reg 		 memory;

  assign t = the;
  assign tt = thethe;
  assign ttt = thethethe;
  assign tttt = thethethethe;
  assign ttttt = thethethethethe;
  assign m = memory;
  
  always @ ( posedge clk )
  begin
    if ( reset ) begin
      // Asynchronous reset when reset goes high
      the = 1;
      thethe = 0;
      thethethe = 0;
      thethethethe = 0;
      thethethethethe = 0;
      memory = 0;
    end else begin
      // Assign D to Q on positive clock edge
      the = ~the;
      if ( the ) begin
      	 thethe = ~ thethe; 
        if ( thethe ) begin
          	thethethe = ~thethethe;
          if ( thethethe ) begin
            thethethethe = ~ thethethethe;
            if ( thethethethe ) begin
            thethethethethe = ~ thethethethethe;
              if ( thethethethethe ) begin
                	memory = b;
              end else begin
                	memory = memory;
              end
          end else begin
            thethethethethe = thethethethethe;
          end
          end else begin
            thethethethe = thethethethe;
          end
        end else begin
          thethethe = thethethe;
        end
      end else begin
         thethe = thethe;
      end
    end
  end
endmodule