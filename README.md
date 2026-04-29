# CISC360-TM

## The tape

This is quite likely to be wrong, at this point, as I am mostly writing this from
memory, without looking back at all of the files.

If all is going well, exactly one tape segment is 'active' at any given time.
The value of the active tape segment will be sent out onto the Value bus.

If the Write flag is set, the value of the active tape segment will be set to
whatever is present on the Data bus.

The intended sequence of events is:
1. Read
2. Write
3. Shift

The shift operation, however, takes place partially during the other two, so as
not to get confused.  A secondary activation bit is set in the current active
segment, and then the primary activation bit is set in the neighbouring segment
(in accordance with which of SHL and SHR is set).


## The state machine

### States

This is really what still needs to be figured out.  TODO

Phases:
1. Read: This should also include looking up (and likely storing, likely in some
   global registers) what needs to be done in the active state's internal table
2. Write: Write the stored write value into the currently active tape segment
3. Shift: As per the stored shift direction
   - Maybe this should also include activating the next state; that seems kind
     of like a weird shift, and it needs to happen

Some other ideas, beyond globally storing what to do, given what's been read:
- 16 wires out from each state, corresponding to each of the tape symbols,
  connecting to the target states
- 16 dipswitches to indicate R/L for each tape symbol
- 16 wires connecting directly to a global array of four bit wide tape symbols
  - i.e. from the read value on the given state to the value to be written
- A way to build subroutines out of hardware
  - This one, I'm really not sure of.  On the one hand, it could easily save us
    a tonne of time and effort; on the other hand, it would make simply reading
    off of the compiled UTM *much* harder.  I suppose we could read off of the
    original, but the amount of shorthands will make that harder.

## Initialisation

A special "init" state will need to be developed (TODO), which will read through
a ROM (which can be loaded into Digital from a file), and write its contents
onto the tape, and then reset back to the left end marker.
