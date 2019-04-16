keyconfig_data = \
[("Screen",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
    ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
    ("screen.screen_full_area", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area",
     {"type": 'SPACE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("use_hide_panels", True),
       ],
      },
     ),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.region_quadview", {"type": 'Q', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("screen.repeat_last", {"type": 'R', "value": 'PRESS', "shift": True}, None),
    ("file.execute", {"type": 'RET', "value": 'PRESS'}, None),
    ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
    ("file.cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True}, None),
    ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("render.render",
     {"type": 'F12', "value": 'PRESS'},
     {"properties":
      [("use_viewport", True),
       ],
      },
     ),
    ("render.render",
     {"type": 'F12', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("animation", True),
       ("use_viewport", True),
       ],
      },
     ),
    ("render.view_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("render.view_show", {"type": 'F11', "value": 'PRESS'}, None),
    ("render.play_rendered_anim", {"type": 'F11', "value": 'PRESS', "ctrl": True}, None),
    ("screen.redo_last", {"type": 'W', "value": 'PRESS', "alt": True}, None),
    ],
   },
  ),
 ("Mesh",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("wm.call_menu",
     {"type": 'C', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MESH_MT_CopyFaceSettings'),
       ],
      },
     ),
    ("mesh.loopcut_slide",
     {"type": 'R', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("TRANSFORM_OT_edge_slide",
        [("release_confirm", False),
         ],
        ),
       ],
      },
     ),
    ("mesh.offset_edge_loops_slide",
     {"type": 'R', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("TRANSFORM_OT_edge_slide",
        [("release_confirm", False),
         ],
        ),
       ],
      },
     ),
    ("mesh.inset", {"type": 'I', "value": 'PRESS'}, None),
    ("mesh.bevel",
     {"type": 'B', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("vertex_only", False),
       ],
      },
     ),
    ("mesh.bevel",
     {"type": 'B', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("vertex_only", True),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("type", 'VERT'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("type", 'EDGE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("type", 'FACE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'ONE', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_extend", True),
       ("type", 'VERT'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'TWO', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_extend", True),
       ("type", 'EDGE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'THREE', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_extend", True),
       ("type", 'FACE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'ONE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_expand", True),
       ("type", 'VERT'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'TWO', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_expand", True),
       ("type", 'EDGE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'THREE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_expand", True),
       ("type", 'FACE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'ONE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("use_extend", True),
       ("use_expand", True),
       ("type", 'VERT'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'TWO', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("use_extend", True),
       ("use_expand", True),
       ("type", 'EDGE'),
       ],
      },
     ),
    ("mesh.select_mode",
     {"type": 'THREE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("use_extend", True),
       ("use_expand", True),
       ("type", 'FACE'),
       ],
      },
     ),
    ("mesh.loop_select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("extend", False),
       ("deselect", False),
       ("toggle", False),
       ],
      },
     ),
    ("mesh.loop_select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("extend", False),
       ("deselect", False),
       ("toggle", True),
       ],
      },
     ),
    ("mesh.edgering_select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("extend", False),
       ("deselect", False),
       ("toggle", False),
       ],
      },
     ),
    ("mesh.edgering_select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("extend", False),
       ("deselect", False),
       ("toggle", True),
       ],
      },
     ),
    ("mesh.shortest_path_pick",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("use_fill", False),
       ],
      },
     ),
    ("mesh.shortest_path_pick",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("use_fill", True),
       ],
      },
     ),
    ("mesh.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("mesh.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("mesh.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("mesh.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("mesh.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("mesh.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("mesh.select_next_item", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("mesh.select_prev_item", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("mesh.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
    ("mesh.select_linked_pick",
     {"type": 'L', "value": 'PRESS'},
     {"properties":
      [("deselect", False),
       ],
      },
     ),
    ("mesh.select_linked_pick",
     {"type": 'L', "value": 'PRESS', "shift": True},
     {"properties":
      [("deselect", True),
       ],
      },
     ),
    ("mesh.select_mirror", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("wm.call_menu",
     {"type": 'G', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_select_similar'),
       ],
      },
     ),
    ("mesh.hide",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("mesh.hide",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("mesh.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
    ("mesh.normals_make_consistent",
     {"type": 'N', "value": 'PRESS', "shift": True},
     {"properties":
      [("inside", False),
       ],
      },
     ),
    ("mesh.normals_make_consistent",
     {"type": 'N', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("inside", True),
       ],
      },
     ),
    ("mesh.flip_normals", {"type": 'N', "value": 'PRESS', "alt": True}, None),
    ("wm.tool_set_by_id",
     {"type": 'E', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'builtin.extrude_along_normals'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'E', "value": 'PRESS', "alt": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_extrude'),
       ],
      },
     ),
    ("transform.edge_crease", {"type": 'E', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("mesh.fill", {"type": 'F', "value": 'PRESS', "alt": True}, None),
    ("mesh.quads_convert_to_tris",
     {"type": 'T', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("quad_method", 'BEAUTY'),
       ("ngon_method", 'BEAUTY'),
       ],
      },
     ),
    ("mesh.quads_convert_to_tris",
     {"type": 'T', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("quad_method", 'FIXED'),
       ("ngon_method", 'CLIP'),
       ],
      },
     ),
    ("mesh.tris_convert_to_quads", {"type": 'J', "value": 'PRESS', "alt": True}, None),
    ("mesh.rip_move",
     {"type": 'V', "value": 'PRESS'},
     {"properties":
      [("MESH_OT_rip",
        [("use_fill", False),
         ],
        ),
       ],
      },
     ),
    ("mesh.rip_move",
     {"type": 'V', "value": 'PRESS', "alt": True},
     {"properties":
      [("MESH_OT_rip",
        [("use_fill", True),
         ],
        ),
       ],
      },
     ),
    ("mesh.rip_edge_move", {"type": 'D', "value": 'PRESS', "alt": True}, None),
    ("mesh.merge", {"type": 'M', "value": 'PRESS', "alt": True}, None),
    ("transform.shrink_fatten", {"type": 'S', "value": 'PRESS', "alt": True}, None),
    ("mesh.edge_face_add", {"type": 'F', "value": 'PRESS'}, None),
    ("mesh.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_mesh_add'),
       ],
      },
     ),
    ("mesh.separate", {"type": 'P', "value": 'PRESS'}, None),
    ("mesh.split", {"type": 'Y', "value": 'PRESS'}, None),
    ("mesh.vert_connect_path", {"type": 'J', "value": 'PRESS'}, None),
    ("mesh.point_normals", {"type": 'L', "value": 'PRESS', "alt": True}, None),
    ("transform.vert_slide", {"type": 'V', "value": 'PRESS', "shift": True}, None),
    ("mesh.dupli_extrude_cursor",
     {"type": 'RIGHTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("rotate_source", True),
       ],
      },
     ),
    ("mesh.dupli_extrude_cursor",
     {"type": 'RIGHTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("rotate_source", False),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'X', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_delete'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'DEL', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_delete'),
       ],
      },
     ),
    ("mesh.dissolve_mode", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
    ("mesh.dissolve_mode", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
    ("mesh.knife_tool",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("use_occlude_geometry", True),
       ("only_selected", False),
       ],
      },
     ),
    ("object.vertex_parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_context_menu'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'F', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_faces'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'E', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_edges'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'V', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_vertices'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'H', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_hook'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'U', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_uv_map'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'G', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_vertex_group'),
       ],
      },
     ),
    ("object.vertex_group_remove_from", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("wm.call_menu_pie",
     {"type": 'O', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_proportional_editing_falloff_pie'),
       ],
      },
     ),
    ("wm.context_toggle_enum",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'tool_settings.proportional_edit'),
       ("value_1", 'DISABLED'),
       ("value_2", 'ENABLED'),
       ],
      },
     ),
    ("wm.context_toggle_enum",
     {"type": 'O', "value": 'PRESS', "alt": True},
     {"properties":
      [("data_path", 'tool_settings.proportional_edit'),
       ("value_1", 'DISABLED'),
       ("value_2", 'CONNECTED'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_edit_mesh_select_mode'),
       ],
      },
     ),
    ],
   },
  ),
 ("Object Non-modal",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_shade_of'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_of'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_object_mode_of'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'SPACE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_manipulator_of'),
       ],
      },
     ),
    ("object.mode_set",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("mode", 'EDIT'),
       ("toggle", True),
       ],
      },
     ),
    ("view3d.object_mode_pie_or_toggle",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ],
   },
  ),
 ("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("view3d.cursor3d", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ("transform.translate",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True},
     {"properties":
      [("cursor_transform", True),
       ("release_confirm", True),
       ],
      },
     ),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview_remove_from", {"type": 'M', "value": 'PRESS'}, None),
    ("view3d.rotate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected",
     {"type": 'C', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'NORTH', "alt": True},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'SOUTH', "alt": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'EAST', "alt": True},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'WEST', "alt": True},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle",
     {"type": 'C', "value": 'PRESS'},
     {    "active":False,
      },
     ),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
    ("transform.rotate",
     {"type": 'R', "value": 'PRESS'},
     {    "active":False,
      },
     ),
    ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
    ("transform.bend",
     {"type": 'W', "value": 'PRESS', "shift": True},
     {    "active":False,
      },
     ),
    ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", False),
       ],
      },
     ),
    ("object.transform_axis_target", {"type": 'T', "value": 'PRESS', "shift": True}, None),
    ("transform.skin_resize", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo_tool'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo_tool'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_shading_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'Q', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.select_lasso'),
       ("cycle", False),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.move'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.rotate'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'R', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.scale'),
       ],
      },
     ),
    ("transform.select_orientation", {"type": 'Q', "value": 'PRESS', "alt": True}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
