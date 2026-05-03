# Usage: cat <machine_yaml_file_name> | python3 statemachine.py > statemachine.dig

import yaml
import html

TAPE_SYMBOLS = [
        '⊢', '0' , '1' , '#' , '00', '01', '10', '11',
        '⊔', '#0', '#1', '⊔0', '⊔1', 'H' , 'H0', 'H1'
]

INPUTS = """\
    <!-- Inputs -->
    <visualElement>
      <elementName>In</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>Start</string>
        </entry>
      </elementAttributes>
      <pos x="80" y="-140"/>
    </visualElement>
    <visualElement>
      <elementName>In</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>Activating</string>
        </entry>
      </elementAttributes>
      <pos x="80" y="-100"/>
    </visualElement>
    <visualElement>
      <elementName>In</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>Lookup</string>
        </entry>
        <entry>
          <string>Bits</string>
          <int>16</int>
        </entry>
      </elementAttributes>
      <pos x="80" y="-60"/>
    </visualElement>

"""

OUTPUTS = """\
    <!-- Outputs -->
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="620" y="-140"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="620" y="-100"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>Γ&apos;</string>
        </entry>
      </elementAttributes>
      <pos x="620" y="-60"/>
    </visualElement>

 """

 SHIFT_OUTPUT_TUNNELS = """\<!-- Shift output tunnels -->
 <visualElement>
   <elementName>Tunnel</elementName>
   <elementAttributes>
     <entry>
       <string>rotation</string>
       <rotation rotation="2"/>
     </entry>
     <entry>
       <string>NetName</string>
       <string>shl</string>
     </entry>
   </elementAttributes>
   <pos x="600" y="-140"/>
 </visualElement>
 <visualElement>
   <elementName>Tunnel</elementName>
   <elementAttributes>
     <entry>
       <string>rotation</string>
       <rotation rotation="2"/>
     </entry>
     <entry>
       <string>NetName</string>
       <string>shr</string>
     </entry>
   </elementAttributes>
   <pos x="600" y="-100"/>
 </visualElement>

"""

GAMMA_OUTPUT_TUNNELS_AND_SPLITTER = """\
    <!-- Gamma output tunnels and splitter -->
    <visualElement>
      <elementName>Splitter</elementName>
      <elementAttributes>
        <entry>
          <string>mirror</string>
          <boolean>true</boolean>
        </entry>
        <entry>
          <string>Input Splitting</string>
          <string>1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1</string>
        </entry>
        <entry>
          <string>Output Splitting</string>
          <string>16</string>
        </entry>
      </elementAttributes>
      <pos x="540" y="-60"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>H1</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-60"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>H0</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-80"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>H</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-100"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>⊔1</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-120"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>⊔0</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-140"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>#1</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-160"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>#0</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-180"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>⊔</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-200"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>11</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-220"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>10</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-240"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>01</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-260"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>00</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-280"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>#</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-300"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>1</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-320"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>0</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-340"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>⊢</string>
        </entry>
      </elementAttributes>
      <pos x="520" y="-360"/>
    </visualElement>

 """

 BOTTOM_OUTPUTS = """\
 <!-- Bottom outputs -->
 <visualElement>
   <elementName>Out</elementName>
   <elementAttributes>
     <entry>
       <string>Label</string>
       <string>✓</string>
     </entry>
     <entry>
       <string>rotation</string>
       <rotation rotation="3"/>
     </entry>
   </elementAttributes>
   <pos x="280" y="-160"/>
 </visualElement>
 <visualElement>
   <elementName>Out</elementName>
   <elementAttributes>
     <entry>
       <string>Label</string>
       <string>✗</string>
     </entry>
     <entry>
       <string>rotation</string>
       <rotation rotation="3"/>
     </entry>
   </elementAttributes>
   <pos x="320" y="-160"/>
 </visualElement>

 """

BOTTOM_OUTPUT_TUNNELS = """\
    <!-- Bottom output tunnels -->
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="1"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>accept</string>
        </entry>
      </elementAttributes>
      <pos x="280" y="-180"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="1"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>reject</string>
        </entry>
      </elementAttributes>
      <pos x="320" y="-180"/>
    </visualElement>

"""

def main():
        machine_yaml = yaml.load(input())

        visElems = (
                make_states(machine_yaml) +
                INPUTS +
                make_input_tunnels(machine_yaml["start state"]) +
                OUTPUTS +
                SHIFT_OUTPUT_TUNNELS +
                GAMMA_OUTPUT_TUNNELS_AND_SPLITTER +
                BOTTOM_OUTPUTS +
                BOTTOM_OUTPUT_TUNNELS
        )
        wires = make_wires(len(machine_yaml)) + NON_VARIAT_WIRES

        final = f"""\
<?xml version="1.0" encoding="utf-8"?>
<circuit>
  <version>2</version>
  <attributes>
    <entry>
      <string>shapeType</string>
      <shapeType>LAYOUT</shapeType>
    </entry>
    <entry>
      <string>romContent</string>
      <romList>
        <roms/>
      </romList>
    </entry>
    <entry>
      <string>Height</string>
      <int>5</int>
    </entry>
    <entry>
      <string>Width</string>
      <int>7</int>
    </entry>
  </attributes>
  <visualElements>
{visElems}
  </visualElements>
  <wires>
{wires}
  </wires>
  <measurementOrdering/>
</circuit>
"""

        print(final)

def make_states(machine_yaml):
        return "\n\n".join([
                make_state(name, flatten(trans), i) +
                make_bottom_tunnels(name, flatten(trans), i) +
                make_left_tunnels(name, flatten(trans), i) +
                make_right_tunnels(name, flatten(trans), i)
                for i, (name, trans) in enumerate(machine_yaml["table"].items())
        ])

def make_state(name, trans, i):
        directions = "".join(
                ["0" if trans[sym].haskey("R") else "1" for sym in TAPE_SYMBOLS]
        )
        return f"""\
    <!-- The state -->
    <visualElement>
      <elementName>state.dig</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>{html.escape(name)}</string>
        </entry>
        <entry>
          <string>generic</string>
          <string>shift := 0b{directions};</string>
        </entry>
      </elementAttributes>
      <pos x="0" y="{200 * i}"/>
    </visualElement>

 """

 def flatten(trans):
        out = {}
        for k, v in trans.items():
                if isinstance(k, str):
                        out[k] = v
                        continue
                for sym in k:
                        out[sym] = v
        return out

def make_bottom_tunnels(name, trans, i):
        out = "    <!-- The bottom tunnels -->\n"
        for j, sym in enumerate(TAPE_SYMBOLS):
                gamma_prime = html.escape(trans['sym'].get('write', sym))
                # TODO: does dict.get() fail if key is present but undefined?
                q_prime = html.escape(
                        trans['sym'].get('R', trans['sym'].get('L', name)))
                out += f"""\
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="3"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>{gamma_prime}</string>
        </entry>
      </elementAttributes>
      <pos x="{20 + 40 * j}" y="{120 + 200 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="3"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>{q_prime}</string>
        </entry>
      </elementAttributes>
      <pos x="{40 + 40 * j}" y="{120 + 200 * i}"/>
    </visualElement>
"""
        return out + "\n"

def make_left_tunnels(name, trans, i):
        return f"""\
    <!-- The left tunnels -->
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>{html.escape(name)}</string>
        </entry>
      </elementAttributes>
      <pos x="-20" y="{200 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>act</string>
        </entry>
      </elementAttributes>
      <pos x="-20" y="{20 + 200 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>look</string>
        </entry>
      </elementAttributes>
      <pos x="-20" y="{40 + 200 * i}"/>
    </visualElement>

 """

def make_right_tunnels(name, trans, i):
        return f"""\
    <!-- The right tunnels -->
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>shl</string>
        </entry>
      </elementAttributes>
      <pos x="680" y="{200 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>shr</string>
        </entry>
      </elementAttributes>
      <pos x="680" y="{40 + 200 * i}"/>
    </visualElement>

 """

def make_input_tunnels(start_state):
        return f"""\
    <!-- Input tunnels -->
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>{html.escape(start_state)}</string>
        </entry>
      </elementAttributes>
      <pos x="100" y="-140"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>act</string>
        </entry>
      </elementAttributes>
      <pos x="100" y="-100"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>look</string>
        </entry>
      </elementAttributes>
      <pos x="100" y="-60"/>
    </visualElement>

 """

def make_wires(state_count):
        out = "<!-- State related wires (multiple; n) -->\n"
        for i in range(state_count):
                out += make_wire_set(i)

def make_wire_set(i):
        out = f"""
    <wire><!-- name -->
      <p1 x="-20" y="{200 * i}"/>
      <p2 x="0" y="{200 * i}"/>
    </wire>
    <wire><!-- act -->
      <p1 x="-20" y="{20 + 200 * i}"/>
      <p2 x="0" y="{20 + 200 * i}"/>
    </wire>
    <wire><!-- look -->
      <p1 x="-20" y="{40 + 200 * i}"/>
      <p2 x="0" y="{40 + 200 * i}"/>
    </wire>

    <wire><!-- SHL -->
      <p1 x="660" y="{200 * i}"/>
      <p2 x="680" y="{200 * i}"/>
    </wire>
    <wire><!-- SHR -->
      <p1 x="660" y="{40 + 200 * i}"/>
      <p2 x="680" y="{40 + 200 * i}"/>
    </wire>

 """
        for j in len(TAPE_SYMBOLS):
                gamma_prime = html.escape(trans['sym'].get('write', sym))
                q_prime = html.escape(
                        trans['sym'].get('R', trans['sym'].get('L', name)))
                out += f"""\
    <wire>
      <p1 x="{20 + 40 * j}" y="{100 + 200 * i}"/>
      <p2 x="{20 + 40 * j}" y="{120 + 200 * i}"/>
    </wire>
    <wire>
      <p1 x="{40 + 40 * j}" y="{100 + 200 * i}"/>
      <p2 x="{40 + 40 * j}" y="{120 + 200 * i}"/>
    </wire>
"""
        return out + "\n"


if __name__ == "__main__":
        main()
