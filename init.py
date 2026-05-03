# Usage: cat <tape_file_name> | python3 init.py > init.dig

OUTPUT_PINS = """\

    <!-- Output pins -->
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>rotation</string>
          <rotation rotation="2"/>
        </entry>
        <entry>
          <string>NetName</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="780" y="20"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="20"/>
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
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="780" y="60"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="60"/>
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
      <pos x="780" y="100"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>left</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="100"/>
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
      <pos x="780" y="140"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>0</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="140"/>
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
      <pos x="780" y="180"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>1</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="180"/>
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
      <pos x="780" y="220"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>#</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="220"/>
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
          <string>done</string>
        </entry>
      </elementAttributes>
      <pos x="780" y="260"/>
    </visualElement>
    <visualElement>
      <elementName>Out</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>done</string>
        </entry>
      </elementAttributes>
      <pos x="800" y="260"/>
    </visualElement>

"""
PREDONE_RESET_STATE = """\
    <!-- PREDONE/RESET STATE -->
    <visualElement>
      <elementName>state.dig</elementName>
      <elementAttributes>
        <entry>
          <string>generic</string>
          <string>shift := 0x8000;</string>
        </entry>
      </elementAttributes>
      <pos x="-500" y="360"/>
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
          <string>predone</string>
        </entry>
      </elementAttributes>
      <pos x="-520" y="360"/>
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
      <pos x="-580" y="400"/>
    </visualElement>

    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="180" y="360"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="180" y="400"/>
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
          <string>⊢</string>
        </entry>
      </elementAttributes>
      <pos x="-480" y="480"/>
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
          <string>0</string>
        </entry>
      </elementAttributes>
      <pos x="-440" y="480"/>
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
          <string>predone</string>
        </entry>
      </elementAttributes>
      <pos x="-420" y="480"/>
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
          <string>1</string>
        </entry>
      </elementAttributes>
      <pos x="-400" y="480"/>
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
          <string>predone</string>
        </entry>
      </elementAttributes>
      <pos x="-380" y="480"/>
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
          <string>#</string>
        </entry>
      </elementAttributes>
      <pos x="-360" y="480"/>
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
          <string>predone</string>
        </entry>
      </elementAttributes>
      <pos x="-340" y="480"/>
    </visualElement>

"""
DONE_RESET_STATE = """\
    <!-- DONE/RESET STATE -->
    <visualElement>
      <elementName>state.dig</elementName>
      <elementAttributes>
        <entry>
          <string>generic</string>
          <string>shift := 0xFFFF;</string>
        </entry>
      </elementAttributes>
      <pos x="-500" y="640"/>
    </visualElement>

    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="180" y="640"/>
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
          <string>0</string>
        </entry>
      </elementAttributes>
      <pos x="-440" y="760"/>
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
          <string>done</string>
        </entry>
      </elementAttributes>
      <pos x="-420" y="760"/>
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
          <string>1</string>
        </entry>
      </elementAttributes>
      <pos x="-400" y="760"/>
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
          <string>done</string>
        </entry>
      </elementAttributes>
      <pos x="-380" y="760"/>
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
          <string>#</string>
        </entry>
      </elementAttributes>
      <pos x="-360" y="760"/>
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
          <string>done</string>
        </entry>
      </elementAttributes>
      <pos x="-340" y="760"/>
    </visualElement>

"""

NON_VARIAT_WIRES = """\
    <!-- non-variat -->
    <wire><!-- done from q -->
      <p1 x="-520" y="640"/>
      <p2 x="-500" y="640"/>
    </wire>
    <wire><!-- done SHL -->
      <p1 x="160" y="640"/>
      <p2 x="180" y="640"/>
    </wire>
    <wire><!-- done to out -->
      <p1 x="780" y="260"/>
      <p2 x="800" y="260"/>
    </wire>
    <wire><!-- start.Acto to Action -->
      <p1 x="420" y="140"/>
      <p2 x="460" y="140"/>
    </wire>
    <wire><!-- 0 to out -->
      <p1 x="780" y="140"/>
      <p2 x="800" y="140"/>
    </wire>
    <wire><!-- Action in to split -->
      <p1 x="300" y="140"/>
      <p2 x="320" y="140"/>
    </wire>
    <wire><!-- split to start.Acti -->
      <p1 x="320" y="140"/>
      <p2 x="340" y="140"/>
    </wire>
    <wire><!-- above from start.fqo -->
      <p1 x="440" y="80"/>
      <p2 x="500" y="80"/>
    </wire>
    <wire><!-- predone SHR -->
      <p1 x="160" y="400"/>
      <p2 x="180" y="400"/>
    </wire>
    <wire><!-- Lookup to split -->
      <p1 x="-580" y="400"/>
      <p2 x="-540" y="400"/>
    </wire>
    <wire><!-- split to predone.Lookup -->
      <p1 x="-540" y="400"/>
      <p2 x="-500" y="400"/>
    </wire>
    <wire><!-- SHL to out -->
      <p1 x="780" y="20"/>
      <p2 x="800" y="20"/>
    </wire>
    <wire><!-- to done.Activating -->
      <p1 x="-560" y="660"/>
      <p2 x="-500" y="660"/>
    </wire>
    <wire><!-- zigzag between predone and done -->
      <p1 x="-520" y="600"/>
      <p2 x="-460" y="600"/>
    </wire>
    <wire><!-- # to out -->
      <p1 x="780" y="220"/>
      <p2 x="800" y="220"/>
    </wire>
    <wire><!-- ⊢ -->
      <p1 x="560" y="160"/>
      <p2 x="580" y="160"/>
    </wire>
    <wire><!-- ⊢ to out -->
      <p1 x="780" y="100"/>
      <p2 x="800" y="100"/>
    </wire>
    <wire><!-- predone from q -->
      <p1 x="-520" y="360"/>
      <p2 x="-500" y="360"/>
    </wire>
    <wire><!-- predone SHL -->
      <p1 x="160" y="360"/>
      <p2 x="180" y="360"/>
    </wire>
    <wire><!-- done.Lookup -->
      <p1 x="-540" y="680"/>
      <p2 x="-500" y="680"/>
    </wire>
    <wire><!-- long -->
      <p1 x="-560" y="240"/>
      <p2 x="320" y="240"/>
    </wire>
    <wire><!-- short near long on right -->
      <p1 x="320" y="240"/>
      <p2 x="440" y="240"/>
    </wire>
    <wire><!-- 1 to out -->
      <p1 x="780" y="180"/>
      <p2 x="800" y="180"/>
    </wire>
    <wire><!-- fqo short -->
      <p1 x="420" y="120"/>
      <p2 x="440" y="120"/>
    </wire>
    <wire><!-- first SHR -->
      <p1 x="560" y="120"/>
      <p2 x="580" y="120"/>
    </wire>
    <wire><!-- fqi -->
      <p1 x="320" y="120"/>
      <p2 x="340" y="120"/>
    </wire>
    <wire><!-- SHR to out -->
      <p1 x="780" y="60"/>
      <p2 x="800" y="60"/>
    </wire>
    <wire><!-- predone.Activating -->
      <p1 x="-560" y="380"/>
      <p2 x="-500" y="380"/>
    </wire>
    <wire><!-- vertical from Action in split -->
      <p1 x="320" y="140"/>
      <p2 x="320" y="240"/>
    </wire>
    <wire><!-- 0 Q' predone -->
      <p1 x="-420" y="460"/>
      <p2 x="-420" y="480"/>
    </wire>
    <wire><!-- 0 Q' done -->
      <p1 x="-420" y="740"/>
      <p2 x="-420" y="760"/>
    </wire>
    <wire><!-- # G' predone -->
      <p1 x="-360" y="460"/>
      <p2 x="-360" y="480"/>
    </wire>
    <wire><!-- # G' done -->
      <p1 x="-360" y="740"/>
      <p2 x="-360" y="760"/>
    </wire>
    <wire><!-- small vertical between real states -->
      <p1 x="-520" y="600"/>
      <p2 x="-520" y="640"/>
    </wire>
    <wire><!-- long vertical between real states -->
      <p1 x="-460" y="460"/>
      <p2 x="-460" y="600"/>
    </wire>
    <wire><!-- shorter Action vertical (top left) -->
      <p1 x="-560" y="240"/>
      <p2 x="-560" y="380"/>
    </wire>
    <wire><!-- longer Action vertical -->
      <p1 x="-560" y="380"/>
      <p2 x="-560" y="660"/>
    </wire>
    <wire><!-- 1 G' predone -->
      <p1 x="-400" y="460"/>
      <p2 x="-400" y="480"/>
    </wire>
    <wire><!-- 1 G' done -->
      <p1 x="-400" y="740"/>
      <p2 x="-400" y="760"/>
    </wire>
    <wire><!-- # Q' predone -->
      <p1 x="-340" y="460"/>
      <p2 x="-340" y="480"/>
    </wire>
    <wire><!-- # Q' done -->
      <p1 x="-340" y="740"/>
      <p2 x="-340" y="760"/>
    </wire>
    <wire><!-- little from q near top -->
      <p1 x="500" y="80"/>
      <p2 x="500" y="100"/>
    </wire>
    <wire><!-- 0 G' predone -->
      <p1 x="-440" y="460"/>
      <p2 x="-440" y="480"/>
    </wire>
    <wire><!-- 0 G' done -->
      <p1 x="-440" y="740"/>
      <p2 x="-440" y="760"/>
    </wire>
    <wire><!--vertical fqo to from q -->
      <p1 x="440" y="80"/>
      <p2 x="440" y="120"/>
    </wire>
    <wire><!-- 1 Q' predone -->
      <p1 x="-380" y="460"/>
      <p2 x="-380" y="480"/>
    </wire>
    <wire><!-- 1 Q' done -->
      <p1 x="-380" y="740"/>
      <p2 x="-380" y="760"/>
    </wire>
    <wire><!-- long Lookup vertical -->
      <p1 x="-540" y="400"/>
      <p2 x="-540" y="680"/>
    </wire>
    <wire><!-- ⊢ G' predone -->
      <p1 x="-480" y="460"/>
      <p2 x="-480" y="480"/>
    </wire>
"""

def main():
        init_tape = [sym for sym in input() if sym in {'0', '1', '#'}]
        visElems = (
                OUTPUT_PINS +
                make_main_init_states(init_tape) +
                PREDONE_RESET_STATE +
                DONE_RESET_STATE
        )
        wires = make_wires(init_tape) + NON_VARIAT_WIRES


        final = f"""\
<?xml version="1.0" encoding="utf-8"?>
<circuit>
  <version>2</version>
  <attributes/>
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

FIRST_STATE = """\
    <!-- MAIN INIT STATES -->
    <visualElement>
      <elementName>Const</elementName>
      <elementAttributes>
        <entry>
          <string>Value</string>
          <long>0</long>
        </entry>
      </elementAttributes>
      <pos x="320" y="120"/>
    </visualElement>
    <visualElement>
      <elementName>In</elementName>
      <elementAttributes>
        <entry>
          <string>Label</string>
          <string>Action</string>
        </entry>
      </elementAttributes>
      <pos x="300" y="140"/>
    </visualElement>
    <visualElement>
      <elementName>start.dig</elementName>
      <elementAttributes/>
      <pos x="340" y="120"/>
    </visualElement>
    <visualElement>
      <elementName>initstate.dig</elementName>
      <elementAttributes/>
      <pos x="460" y="100"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="120"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>⊢</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="160"/>
    </visualElement>
"""
def make_main_init_states(init_tape):
        most = "\n".join([make_main_init_state(i, sym)
                for i, sym in enumerate(init_tape[:-1])])

        i = len(init_tape) -1
        sym = init_tape[-1]
        return FIRST_STATE + most + f"""\n\
    <visualElement>
      <elementName>initstate.dig</elementName>
      <elementAttributes/>
      <pos x="460" y="{200 + 100 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHL</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="{220 + 100 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>{sym}</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="{260 + 100 * i}"/>
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
          <string>predone</string>
        </entry>
      </elementAttributes>
      <pos x="500" y="{320 + 100 * i}"/>
    </visualElement>
"""

def make_main_init_state(i, sym):
        return f"""\
    <visualElement>
      <elementName>initstate.dig</elementName>
      <elementAttributes/>
      <pos x="460" y="{200 + 100 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>SHR</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="{220 + 100 * i}"/>
    </visualElement>
    <visualElement>
      <elementName>Tunnel</elementName>
      <elementAttributes>
        <entry>
          <string>NetName</string>
          <string>{sym}</string>
        </entry>
      </elementAttributes>
      <pos x="580" y="{260 + 100 * i}"/>
    </visualElement>
"""


def make_wires(init_tape):
        most = "\n".join([make_wire_set(i) for i in range(len(init_tape) -1)])

        i = len(init_tape) -1
        return most + f"""\n\
    <wire><!-- Action -->
      <p1 x="440" y="{240 + 100 * i}"/>
      <p2 x="460" y="{240 + 100 * i}"/>
    </wire>
    <wire><!-- SHR -->
      <p1 x="560" y="{220 + 100 * i}"/>
      <p2 x="580" y="{220 + 100 * i}"/>
    </wire>
    <wire><!-- sym -->
      <p1 x="560" y="{260 + 100 * i}"/>
      <p2 x="580" y="{260 + 100 * i}"/>
    </wire>
    <wire>
      <p1 x="500" y="{300 + 100 * i}"/>
      <p2 x="500" y="{320 + 100 * i}"/>
    </wire>
"""

def make_wire_set(i):
        return f"""\
    <wire><!-- Action -->
      <p1 x="440" y="{240 + 100 * i}"/>
      <p2 x="460" y="{240 + 100 * i}"/>
    </wire>
    <wire><!-- SHR -->
      <p1 x="560" y="{220 + 100 * i}"/>
      <p2 x="580" y="{220 + 100 * i}"/>
    </wire>
    <wire><!-- sym -->
      <p1 x="560" y="{260 + 100 * i}"/>
      <p2 x="580" y="{260 + 100 * i}"/>
    </wire>

    <wire><!-- vertical Action second to third -->
      <p1 x="440" y="{240 + 100 * i}"/>
      <p2 x="440" y="{340 + 100 * i}"/>
    </wire>
"""


if __name__ == "__main__":
        main()
