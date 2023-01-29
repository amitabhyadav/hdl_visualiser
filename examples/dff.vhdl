-- VHDL code for rising edge D flip flop 

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity reg_dff is
   generic(
      REG_WIDTH : INTEGER);
   port(
      d      : in STD_LOGIC_VECTOR(REG_WIDTH - 1 downto 0);
      clk    : in STD_LOGIC;
      q      : out STD_LOGIC_VECTOR(REG_WIDTH - 1 downto 0));
end reg_dff;
architecture behav of reg_dff is
process(clk)
begin 
    if(rising_edge(clk)) then
      q <= d; 
    end if;       
end process;
end behav
