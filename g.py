"""This module stores globally mutable variables used by this program."""

from __future__ import annotations

import tcod.console
import tcod.context
import tcod.ecs

import game.state

context: tcod.context.Context
"""The window managed by tcod."""

world: tcod.ecs.Registry
"""The activate ECS registry and current session."""

states: list[game.state.State] = []
"""A stack of states with the last item being the active state."""

console: tcod.console.Console
"""The current main console."""