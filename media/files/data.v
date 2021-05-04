`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:22:22 04/07/2021 
// Design Name: 
// Module Name:    data 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module data_compression(
    input clk,
    input start,
    input reset,
    input [0:255] data ,
    output reg [0:255] packed ,
    output reg [0:31] packed_meta ,
    output reg  [0:255] unpacked,
    output reg [0:2] Current_State
);

reg [0:5] counter;
reg [0:4] addr,curr_len;
reg [0:2] Next_State ;

parameter S0=3'b000,
          S1=3'b001,
          S2=3'b010,
          S3=3'b011,
          S4=3'b100,
          S5=3'b101,
          S6=3'b110,
			 S7=3'b111;

//State Change

always @(posedge clk or posedge reset)
begin
	if(reset) Current_State = S0;   
	else Current_State = Next_State;
end

//Control Path

always @(Current_State or start or counter)
begin
	case(Current_State)
		S0: Next_State = (start == 1'b1) ? S1 : S0;
      S1: Next_State = S2;
		S2: Next_State = S3;
		S3: Next_State = (counter == 0) ? S4 : S2;
		S4: Next_State = S5;
      S5: Next_State = S6;
      S6: Next_State = (counter == 0) ? S0 : S5;
    endcase
end

//Data-Path = RTL statement

always @(*)
begin
	case(Current_State)
		S1:
				begin
				    counter = 32;
                addr = 0;
                curr_len = 0;
    		end
		S2: 
            begin
                if(data[8*addr+:8] == 8'b00000000) begin
                    packed_meta[addr] = 0;
                end
                else begin
                    {packed[8*curr_len+:8]} = {data[8*addr+:8]};
                    curr_len = curr_len + 1;
						  packed_meta[addr] = 1;
                end
            end
		S3: 
            begin
                addr = addr + 1;
                counter = counter - 1;
			end
        S4:
            begin
                addr = 0;
                counter = 32;
                curr_len = 0;
            end
        S5:
            begin
                if(packed_meta[addr]==0) begin
                    {unpacked[8*addr+:8]} = 8'b00000000;
                end
                else begin
                    {unpacked[8*addr+:8]} = {packed[8*curr_len+:8]};
                    curr_len = curr_len + 1;
                end
            end    

        S6:
            begin
                counter = counter - 1;
                addr = addr + 1;
            end    
	endcase
	end
endmodule