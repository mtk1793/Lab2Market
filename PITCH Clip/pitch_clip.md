{
  "movie": {
    "title": "AddManuChain – Mission Critical",
    "totalDuration": 90,
    "resolution": "1920x1080",
    "fps": 30,
    "aspectRatio": "16:9",
    "globalStyle": {
      "fontPrimary": "Segoe UI, system-ui, sans-serif",
      "fontMono": "JetBrains Mono, Consolas, monospace",
      "antiAliasing": true,
      "motionBlur": 0.15
    }
  },

  "segments": [
    {
      "id": 1,
      "label": "SEGMENT 1 — SCENARIO A: CALM OPERATIONS + SUDDEN FAILURE",
      "timeRange": "00:00 – 00:10",
      "startFrame": 0,
      "endFrame": 300,
      "duration": 10,

      "narrative": "We open on a pristine Arctic industrial site on a clear day. Equipment runs perfectly. Our operator stands confidently. Then at second 6, CATASTROPHIC FAILURE strikes — alarms blare, the machine shakes violently, and the crisis begins. But our operator doesn't panic — they have AddManuChain.",

      "background": {
        "type": "gradient_sky",
        "skyTop": "#4a90c2",
        "skyBottom": "#cce4f8",
        "groundTop": "#d8e8d0",
        "groundBottom": "#b8c8a8",
        "horizonLine": "55% from top",
        "mountains": {
          "visible": true,
          "color": "#7a8a9a",
          "snowCaps": true,
          "snowCapColor": "#e8f0f5",
          "opacity": 0.6
        },
        "clouds": {
          "count": 8,
          "color": "rgba(210,220,230,0.4)",
          "movement": "left-to-right at 15px/sec",
          "style": "fluffy, peaceful"
        },
        "lighting": "bright daylight, slight warm cast",
        "transition_0s_to_6s": "no change — beautiful clear day",
        "transition_6s_to_10s": "subtle darkening begins, barely noticeable"
      },

      "camera": {
        "0.0": { "type": "wide_establishing", "position": "center", "zoom": 1.0, "note": "Full scene visible — equipment left, operator center-left" },
        "2.0": { "type": "slow_push", "zoom": 1.0, "target": 1.05, "duration": 4, "note": "Gentle zoom toward equipment and operator" },
        "6.0": { "type": "snap_shake", "intensity": 0.8, "duration": 0.5, "note": "VIOLENT shake on failure — camera rattles" },
        "6.5": { "type": "medium_shot", "zoom": 1.15, "focus": "equipment", "note": "Quick cut closer to see damage" },
        "8.0": { "type": "pan_to_operator", "zoom": 1.1, "duration": 2, "note": "Pan to show operator's calm reaction" }
      },

      "equipment": {
        "position": { "x": "17% from left", "y": "centered on horizon" },
        "size": "13% screen width x 26% screen height",
        "components": {
          "mainBody": {
            "color_gradient": ["#1c4466", "#163852", "#102a3e"],
            "shape": "rounded_rectangle",
            "cornerRadius": 5
          },
          "displayScreen": {
            "position": "top panel",
            "size": "60% of body width x 18% of body height",
            "0s_to_6s": {
              "backgroundColor": "rgba(0,60,30,0.8)",
              "text": "OPERATIONAL",
              "textColor": "#00aa44",
              "font": "bold 12px monospace"
            },
            "6s_to_10s": {
              "backgroundColor": "rgba(60,0,0,0.8)",
              "text": "!! FAILURE !!",
              "textColor": "#ff2222",
              "textAnimation": "blink at 400ms interval"
            }
          },
          "gear": {
            "position": "center of body, 52% from top",
            "radius": "18% of min(width, height)",
            "teeth": 8,
            "color": "#66aacc",
            "0s_to_6s": {
              "rotation": "continuous clockwise at 90deg/sec",
              "status": "smooth, healthy"
            },
            "6s_to_10s": {
              "rotation": "STOPS ABRUPTLY at 6.0s",
              "jerks": "small 2-3 degree twitches at 6.5s, 7.2s",
              "color_change": "#66aacc to #aa6666 over 0.5s"
            }
          },
          "statusLights": {
            "positions": ["top-right", "top-left", "bottom-center"],
            "0s_to_6s": {
              "color": "#00ff44",
              "animation": "gentle pulse, opacity 0.7-1.0, period 2s",
              "glow": { "color": "#00ff44", "blur": 8 }
            },
            "6s_to_10s": {
              "color": "#ff2222",
              "animation": "aggressive flash, on/off at 200ms",
              "glow": { "color": "#ff2222", "blur": 12 }
            }
          },
          "warningBeacon": {
            "visible_from": "6.0s",
            "position": "top center of equipment, extending above",
            "color": "#ff3322",
            "animation": "rotating pulse, opacity sine wave 0-1 at 3Hz",
            "glow": { "blur": 15, "color": "rgba(255,50,30,0.4)" }
          },
          "cracks": {
            "visible_from": "6.3s",
            "level": 1,
            "lines": [
              { "path": "30% from left top → 35% at 20% height → 22% at 38% height", "color": "rgba(255,80,50,0.25)", "width": 1.8 }
            ],
            "animation": "cracks DRAW themselves over 0.4 seconds"
          },
          "pipes": {
            "left": { "position": "40% height", "size": "14x10px" },
            "right": { "position": "50% height", "size": "14x8px" },
            "color": "#1a3850"
          },
          "bolts": {
            "positions": ["top-left", "top-right", "bottom-left", "bottom-right"],
            "radius": 2.5,
            "color": "#2a5a80"
          },
          "shake": {
            "start": "6.0s",
            "6.0_to_7.0": { "intensity": 8, "note": "VIOLENT random x,y offset ±8px" },
            "7.0_to_8.5": { "intensity": 4, "note": "Settling but still shaking" },
            "8.5_to_10.0": { "intensity": 2, "note": "Residual tremor" }
          },
          "smoke": {
            "visible_from": "6.5s",
            "rate": "2 particles/second",
            "particles": {
              "origin": "top 30% of equipment body, random x",
              "color": "rgba(80,80,90,0.15)",
              "size": "4-10px radius",
              "velocity": { "x": "random ±15", "y": "-20 to -40" },
              "lifetime": "1-2 seconds",
              "growth": "radius expands 50% over lifetime"
            }
          }
        }
      },

      "operator": {
        "position": { "x": "28% from left", "y": "standing on ground level (55%)" },
        "scale": "proportional to screen height / 550",
        "0s_to_6s": {
          "pose": "stand_confident",
          "legs": "straight, shoulder width",
          "arms": "relaxed at sides, slight natural sway",
          "head": "upright, looking at equipment",
          "expression": "calm_happy",
          "eyes": "2px radius circles, normal position",
          "mouth": "slight smile arc",
          "hardHat": { "color": "#f7c948" },
          "jacket": {
            "color_gradient": ["#2277bb", "darker 30%"],
            "details": "center zipper line (white 8% opacity), collar band"
          }
        },
        "6s_to_10s": {
          "6.0_to_6.5": {
            "reaction": "startled — slight backward lean",
            "head": "snaps toward equipment",
            "eyes": "widen slightly"
          },
          "6.5_to_8.0": {
            "pose": "alert but calm",
            "body_language": "squares shoulders, stands tall",
            "expression": "focused determination",
            "note": "KEY DETAIL: operator does NOT panic. Shows confidence."
          },
          "8.0_to_10.0": {
            "pose": "preparing to act",
            "right_hand": "moves toward jacket pocket",
            "expression": "confident focus"
          }
        },
        "pocket": {
          "position": "right side of jacket, hip level",
          "0s_to_6s": {
            "glow": true,
            "glowColor": "rgba(13,217,255, oscillating 0.1-0.5 at 5Hz)",
            "glowBlur": 16,
            "note": "Subtle hint that something important is in the pocket"
          },
          "8s_to_10s": {
            "glow_intensity": "INCREASES — oscillating 0.3-0.7",
            "note": "Pocket glow intensifies as hand approaches"
          }
        }
      },

      "text_overlays": {
        "0.0_to_3.0": {
          "title": {
            "text": "SCENARIO A: ON-DEMAND SPARE PARTS",
            "position": "top center",
            "font": "12px uppercase, letter-spacing 2.5px",
            "color": "#99aabb",
            "background": "rgba(0,0,0,0.5)",
            "padding": "6px 16px",
            "borderRadius": 6,
            "animation": "fade in over 0.5s"
          },
          "mainMessage": {
            "text": "Remote Arctic Operation – All Systems Nominal",
            "position": "bottom center, 50px from bottom",
            "font": "bold 24px",
            "color": "#ffffff",
            "textShadow": "0 2px 16px rgba(0,0,0,0.9)",
            "animation": "fade in 0.3s"
          },
          "subMessage": {
            "text": "Digital supply chain active. Critical parts available instantly.",
            "position": "below main message",
            "font": "14px",
            "color": "#cccccc"
          }
        },
        "6.0_to_10.0": {
          "alertOverlay": {
            "text": "⚠️ CRITICAL FAILURE",
            "position": "center screen",
            "font": "bold 28px",
            "color": "#ff2222",
            "background": "rgba(180,20,20,0.85)",
            "border": "2px solid #ff4444",
            "borderRadius": 14,
            "padding": "20px 40px",
            "animation": "scale from 0.7 to 1.0 with cubic-bezier(.17,.67,.35,1.2) over 0.35s",
            "duration": "visible for 2.5 seconds then fade out"
          },
          "subAlert": {
            "text": "Impeller X damaged – production halted!",
            "position": "below alert",
            "font": "13px",
            "color": "#ffcccc"
          },
          "bottomMessage": {
            "text": "Production STOPPED. But operator has a solution...",
            "position": "bottom center",
            "visible_from": "8.0s"
          }
        }
      },

      "hud": {
        "visible_from": "1.0s",
        "fadeIn": "0.5s",
        "timer": {
          "position": "top-left",
          "label": "DOWNTIME",
          "0s_to_6s": { "value": "00:00", "color": "#00ff66" },
          "6s_to_10s": { "value": "counting up in real seconds", "color": "#ff3333", "note": "switches to red immediately on failure" }
        },
        "lossCounter": {
          "position": "top-right",
          "label": "PRODUCTION LOSS",
          "0s_to_6s": { "value": "$0", "color": "#00ff66" },
          "6s_to_10s": { "value": "$0", "color": "#00ff66", "note": "stays at $0 — Scenario A has no losses" }
        }
      },

      "audio": {
        "0.0_to_6.0": {
          "music": "light ambient synth pad, C major, peaceful, volume 20%",
          "sfx": "subtle machinery hum (low drone, 80Hz, volume 5%)"
        },
        "6.0": {
          "sfx_alarm": {
            "type": "3x rapid beeps",
            "frequency": 800,
            "waveform": "square",
            "duration_each": "0.1s",
            "spacing": "140ms",
            "volume": "10%"
          },
          "sfx_impact": {
            "type": "metallic thud",
            "frequency": "200Hz fundamental + 1800Hz harmonic",
            "duration": "0.07s"
          }
        },
        "6.5_to_10.0": {
          "music": "tension rises — add minor key strings underneath, building",
          "sfx": "equipment rattle (continuous, low frequency rumble)"
        }
      },

      "screenEffects": {
        "6.0": {
          "redFlash": { "opacity": 0.4, "duration": "0.35s", "fadeOut": "linear" },
          "screenShake": { "intensity": "±8px", "duration": "0.5s", "decay": "exponential" }
        }
      },

      "particles": {
        "6.5_onward": {
          "smoke": {
            "emitRate": "2/sec from equipment top",
            "color": "rgba(80,80,90,0.15)",
            "size": "4-10px",
            "velocity": "up at 20-40px/s, slight random x drift",
            "lifetime": "1-2s"
          }
        }
      }
    },

    {
      "id": 2,
      "label": "SEGMENT 2 — SCENARIO A: HERO RETRIEVAL + PERFECT INSTALLATION + VICTORY",
      "timeRange": "00:10 – 00:20",
      "startFrame": 300,
      "endFrame": 600,
      "duration": 10,

      "narrative": "The operator calmly reaches into their pocket and retrieves a glowing 3D-printed part. With an epic particle trail, the part floats toward the equipment and installs with a satisfying snap. Equipment roars back to life. Confetti. Victory. $0 in losses. 15 seconds total downtime. AddManuChain saves the day.",

      "background": {
        "0s_to_7s": "same as segment 1 — clear sky, bright daylight",
        "7s_to_10s": "sky brightens slightly — golden hour warmth added, symbolic of success"
      },

      "camera": {
        "0.0": { "type": "medium_shot", "zoom": 1.1, "focus": "operator upper body", "note": "Close enough to see pocket clearly" },
        "0.0_to_3.0": { "type": "slow_track", "movement": "slight right to follow hand to pocket" },
        "3.0": { "type": "pull_back", "zoom": 1.1, "target": 1.0, "duration": 2, "note": "Widen to show part floating toward equipment" },
        "5.0_to_7.0": { "type": "push_in", "zoom": 1.0, "target": 1.15, "focus": "equipment installation point", "note": "Zoom for installation moment" },
        "7.0": { "type": "snap_wide", "zoom": 1.0, "note": "Quick cut to wide shot for victory reveal" },
        "7.5_to_10.0": { "type": "slow_pull_back", "zoom": 1.0, "target": 0.95, "note": "Majestic wide shot of success" }
      },

      "operator": {
        "0.0_to_1.5": {
          "pose": "reaching",
          "right_arm": "extends toward right hip pocket, deliberate confident motion",
          "left_arm": "natural support position",
          "expression": "focused, calm",
          "direction": "facing left (toward equipment)",
          "hand_animation": {
            "0.0_to_0.5": "hand moves to pocket opening",
            "0.5_to_1.0": "fingers curl into pocket, subtle glow increases",
            "1.0_to_1.5": "hand withdraws holding glowing part"
          }
        },
        "1.5_to_3.0": {
          "pose": "hold_up",
          "both_arms": "raised, holding part at head height for inspection",
          "held_part": {
            "visible": true,
            "color": "#00ccff",
            "glow": { "color": "#0dd9ff", "blur": 8 },
            "size": "16x10px at operator scale"
          },
          "expression": "confident nod — single head bob at 2.0s"
        },
        "3.0_to_5.0": {
          "pose": "stand",
          "holdPart": false,
          "note": "Part has been released and is now floating independently",
          "expression": "watching with confidence"
        },
        "7.0_to_10.0": {
          "pose": "thumbs_up",
          "right_arm": "raised, thumb pointing up",
          "left_arm": "relaxed at side",
          "expression": "big smile, eyes bright",
          "body_language": "chest out, proud stance"
        }
      },

      "floatingPart": {
        "active_from": "3.0s",
        "active_to": "5.5s",
        "startPosition": { "x": "operator hand position (~28% screen)", "y": "55% - 70px" },
        "endPosition": { "x": "equipment center (17%)", "y": "equipment opening (55% - 13% height)" },
        "trajectory": "smooth ease-in-out curve, slight arc upward in middle",
        "appearance": {
          "shape": "rounded_rectangle 28x18px",
          "color": "#00ccff",
          "innerHighlight": "rgba(255,255,255,0.3) on top half",
          "glow": {
            "color": "#0dd9ff",
            "blur": "22 + sin(time*8)*10 — pulsing glow",
            "note": "Dramatic pulsing spotlight effect"
          }
        },
        "trailParticles": {
          "emitRate": "15/second along path",
          "color": "#0dd9ff",
          "size": "2-4px",
          "velocity": "random spread ±50px/s x, ±50px/s y, slight upward bias",
          "lifetime": "0.5s",
          "fadeOut": "opacity follows lifetime ratio"
        }
      },

      "installation": {
        "timestamp": "5.5s",
        "alignment_animation": {
          "5.0_to_5.5": "part slows, guide lines appear (thin cyan lines connecting part corners to equipment opening)",
          "guideLineColor": "rgba(0,221,255,0.3)",
          "guideLineStyle": "dashed"
        },
        "snap_moment": {
          "timestamp": "5.5s",
          "flash": { "type": "white", "opacity": 0.8, "duration": "80ms" },
          "sparkExplosion": {
            "count": 25,
            "origin": "equipment installation point",
            "colors": ["#ffffff", "#0dd9ff", "#00ff88"],
            "velocity": "random all directions, 100-220px/s",
            "gravity": 150,
            "lifetime": "0.3-0.8s",
            "type": "spark"
          },
          "audio_clang": {
            "frequency": [200, 1800, 3200],
            "waveforms": ["square", "sawtooth", "square"],
            "durations": [0.07, 0.04, 0.03],
            "note": "Satisfying metallic SNAP sound"
          }
        },
        "equipmentRecovery": {
          "5.5_to_6.0": {
            "statusLight": "red → yellow (transition over 0.3s)",
            "displayText": "INITIALIZING...",
            "gear": "begins slow rotation (10deg/s)"
          },
          "6.0_to_6.5": {
            "statusLight": "yellow → green",
            "displayText": "OPERATIONAL",
            "gear": "accelerates to full speed (90deg/s)",
            "cracks": "DISAPPEAR (fade out 0.3s) — equipment is pristine again",
            "smoke": "stops emitting"
          },
          "6.5": {
            "audio_ding": { "frequency": [1200, 1500], "delay": 150, "waveform": "sine", "volume": "10%" }
          }
        }
      },

      "victory": {
        "start": "7.0s",
        "confetti": {
          "count": 80,
          "origin": "full screen width, top",
          "colors": ["#0dd9ff", "#00ff88", "#f7c948", "#ff66bb", "#aa66ff"],
          "velocity_x": "random ±140px/s",
          "velocity_y": "80-180px/s downward",
          "gravity": 70,
          "size": "3-7px",
          "lifetime": "2.5-3.5s",
          "note": "Professional, not cartoonish — angular shapes, varied colors"
        },
        "triumph_audio": {
          "notes": [
            { "freq": 523, "delay": 0, "dur": 0.25, "note": "C5" },
            { "freq": 659, "delay": 200, "dur": 0.25, "note": "E5" },
            { "freq": 784, "delay": 400, "dur": 0.4, "note": "G5" },
            { "freq": 1047, "delay": 650, "dur": 0.6, "note": "C6" }
          ],
          "waveform": "sine",
          "volume": "9%"
        }
      },

      "text_overlays": {
        "0.0_to_3.0": {
          "mainMessage": "Retrieving pre-certified 3D-printed part…",
          "subMessage": "Digital inventory — no warehouse needed"
        },
        "3.0_to_5.5": {
          "mainMessage": "Installing replacement part…",
          "subMessage": "Perfect fit — certified digital twin"
        },
        "7.0_to_10.0": {
          "mainMessage": "✅ MISSION-CRITICAL SYSTEMS MAINTAINED",
          "subMessage": "Production loss: $0 · Downtime: 15 seconds",
          "font": "bold 26px",
          "animation": "scale pop from 0.8 to 1.0 with bounce"
        }
      },

      "hud": {
        "timer": {
          "0s": "counting from ~4s",
          "5.5s": "STOPS at 00:15",
          "color_at_stop": "#00ff66 with checkmark ✓ appended"
        },
        "lossCounter": {
          "value": "$0",
          "color": "#00ff66",
          "note": "Stays green and at zero the ENTIRE time"
        }
      }
    },

    {
      "id": 3,
      "label": "SEGMENT 3 — TRANSITION + SCENARIO B: SETUP + EQUIPMENT FAILURE",
      "timeRange": "00:20 – 00:30",
      "startFrame": 600,
      "endFrame": 900,
      "duration": 10,

      "narrative": "Screen fades to black. Beat of silence. Then we open on the SAME location, SAME equipment — but this time there's no digital inventory. Only a physical storage unit 200 meters away. The sky already has ominous storm clouds. Equipment is running... then FAILS with the same violent breakdown. But this time, there's no pocket solution. The operator looks toward the distant storage with dread.",

      "transition": {
        "0.0_to_2.0": {
          "type": "fade_to_black",
          "duration": "1.2s fade, then 0.8s pure black",
          "audio": "all sound fades out over 1s, then silence",
          "text_on_black": {
            "text": "But what if you didn't have digital inventory?",
            "font": "18px italic",
            "color": "#666666",
            "position": "center",
            "fadeIn": "0.5s",
            "fadeOut": "0.5s"
          }
        },
        "2.0_to_2.5": {
          "type": "fade_from_black",
          "duration": "0.5s"
        }
      },

      "background": {
        "2.5_to_10.0": {
          "skyTop": "#5599cc fading toward #3a4a5a",
          "skyBottom": "#b8d8f0 fading toward #8899aa",
          "note": "Same scene but MOODIER — color grading is desaturated, cooler",
          "clouds": {
            "count": 14,
            "startColor": "rgba(180,180,190,0.5)",
            "transitionTo": "rgba(80,80,90,0.7) by end of segment",
            "movement": "left-to-right, FASTER than Scenario A (25px/s)",
            "size": "larger than Scenario A — ominous"
          },
          "horizonStormClouds": {
            "visible": true,
            "position": "right side of sky, 10-30% from top",
            "color": "rgba(40,40,50,0.6)",
            "animation": "slowly creeping toward center at 5px/s",
            "note": "Visible threat approaching"
          }
        }
      },

      "camera": {
        "2.5": { "type": "wide_establishing", "zoom": 0.95, "note": "Slightly wider than Scenario A — shows storage unit on right side" },
        "2.5_to_6.0": { "type": "slow_push", "target": 1.02, "note": "Gentle ominous approach" },
        "6.0": { "type": "snap_shake", "intensity": 1.2, "duration": 0.6, "note": "HARDER shake than Scenario A — more violent failure" },
        "7.0_to_10.0": { "type": "slow_pan_right", "note": "Camera pans to reveal the DISTANCE between equipment and storage" }
      },

      "equipment": {
        "2.5_to_6.0": {
          "status": "operational",
          "gear": "rotating normally at 90deg/s",
          "display": "OPERATIONAL in green",
          "note": "Identical to Scenario A opening — equipment is fine"
        },
        "6.0_to_10.0": {
          "failure": {
            "timestamp": "6.0s",
            "shake_intensity": 1.2,
            "shake_duration": "4 seconds (longer than Scenario A!)",
            "status": "error",
            "gear": "JAMS — stops with visible jerk",
            "display": "!! FAILURE !! blinking",
            "cracks": "level 1 appears immediately",
            "smoke": "starts at 0.5 particles/sec",
            "warningBeacon": "activates — red rotating pulse"
          }
        }
      },

      "storageUnit": {
        "visible": true,
        "position": { "x": "72% from left", "y": "on ground level" },
        "size": "14% width x 22% height",
        "appearance": {
          "structure": "small weathered shed with angled roof",
          "walls": "brown-gray (#5a4a3a)",
          "roof": "darker brown (#6a5a4a), triangular",
          "shelves": "3 horizontal lines inside",
          "label": "SPARE PARTS STORAGE (9px bold, above structure)"
        },
        "parts_on_shelves": [
          { "id": 0, "label": "Valve A", "color": "#8899aa", "position": "shelf 2, slot 1" },
          { "id": 1, "label": "Coupling B", "color": "#99887a", "position": "shelf 2, slot 2" },
          { "id": 2, "label": "Flange C", "color": "#7a8899", "position": "shelf 2, slot 3" },
          { "id": 3, "label": "Impeller X", "color": "#00bbee", "position": "shelf 2, slot 4", "note": "The correct part — but hard to distinguish at distance" }
        ],
        "distanceMarker": {
          "visible_from": "8.0s",
          "text": "← 200m →",
          "position": "along dashed path between equipment and storage",
          "color": "rgba(200,200,200,0.3)",
          "font": "10px sans-serif"
        }
      },

      "operator": {
        "2.5_to_6.0": {
          "pose": "stand",
          "expression": "neutral, slightly watchful (looking at sky occasionally)",
          "note": "NO pocket glow — no digital inventory available"
        },
        "6.0_to_7.0": {
          "reaction": "STARTLED — stumbles back half step",
          "expression": "shock, eyes widen",
          "arms": "defensive raise"
        },
        "7.0_to_10.0": {
          "pose": "stand",
          "head": "turns slowly toward storage unit (right)",
          "expression": "dawning_dread — realizes they must walk 200m",
          "body_language": "shoulders drop slightly",
          "struggle": 0.3,
          "note": "This is the moment of 'oh no' — audience sees the distance"
        }
      },

      "text_overlays": {
        "2.5_to_5.5": {
          "title": "SCENARIO B: TRADITIONAL SPARE PARTS",
          "mainMessage": "Remote Arctic Operation – Storm on Horizon",
          "subMessage": "Physical stockpile 200m away. Weather window: 4 hours."
        },
        "6.0_to_8.0": {
          "alert": { "text": "⚠️ CRITICAL FAILURE – Impeller X DAMAGED", "style": "red alert popup" },
          "subAlert": "Production stopped. Losses mounting..."
        },
        "8.0_to_10.0": {
          "mainMessage": "No digital inventory. Must walk to storage.",
          "subMessage": "200 meters away. Storm approaching."
        }
      },

      "hud": {
        "visible_from": "3.0s",
        "timer": { "starts_counting": "6.0s", "color": "red" },
        "lossCounter": {
          "6.0s": "$0",
          "7.0s": "jumps to $10,000 — first minute of downtime",
          "10.0s": "$15,000",
          "lossFlash": { "text": "-$10,000", "timestamp": "7.0s", "color": "#ff4444", "animation": "pop up and fade" }
        }
      },

      "audio": {
        "0.0_to_2.0": "fade to silence",
        "2.5": "low ominous drone begins (D minor pad, volume 10%)",
        "4.0": "distant wind whisper barely audible",
        "6.0": {
          "alarm": {
            "type": "harsher alarm than Scenario A",
            "frequency": 400,
            "waveform": "sawtooth",
            "pattern": "3 beeps, 220ms spacing",
            "duration_each": "0.18s",
            "volume": "12%",
            "note": "Lower pitch, more distressing than Scenario A's 800Hz"
          }
        },
        "8.0": "wind sound begins — low whoosh, building"
      },

      "screenEffects": {
        "6.0": {
          "redFlash": { "opacity": 0.4, "duration": "0.35s" },
          "screenShake": { "intensity": 10, "duration": "0.6s" }
        }
      }
    },

    {
      "id": 4,
      "label": "SEGMENT 4 — SCENARIO B: STORM HITS + DESPERATE WALK BEGINS",
      "timeRange": "00:30 – 00:40",
      "startFrame": 900,
      "endFrame": 1200,
      "duration": 10,

      "narrative": "Weather deteriorates RAPIDLY. Rain starts, wind picks up, temperature plummets to -25°C. The operator begins the 200-meter trek toward the storage unit, fighting against howling wind. Every step is a struggle. They stumble once from a powerful gust. The loss counter climbs relentlessly. Distant thunder rumbles.",

      "background": {
        "sky_transition": "from #3a4a5a/#8899aa to #1a2030/#4a5060 over 10 seconds",
        "clouds": {
          "darkness": "increases from 0.3 to 0.7",
          "movement_speed": "accelerates from 25 to 50px/s (wind increasing)",
          "count": 14,
          "note": "Clouds visibly racing across sky"
        },
        "ground": {
          "color_transition": "from #d0d8c8 toward #6a6a60 (darkening)",
          "snow_accumulation": "slight white tint begins appearing (opacity 0.05 → 0.15)"
        }
      },

      "weather": {
        "rain": {
          "0s": { "rate": 4, "note": "16 particles/sec — light rain beginning" },
          "5s": { "rate": 10, "note": "40 particles/sec — steady rain" },
          "10s": { "rate": 14, "note": "56 particles/sec — heavy rain" },
          "particles": {
            "origin": "full screen width (with wind offset), above viewport",
            "angle": "diagonal — affected by wind (vx = wind*100 + random 30, vy = 450 + random 250)",
            "color": "rgba(170,190,210, 0.25-0.4)",
            "length": "drawn as line from position to position+velocity*0.02",
            "lineWidth": 1.2,
            "lifetime": "0.4-0.6s"
          }
        },
        "snow": {
          "0s": { "rate": 2 },
          "10s": { "rate": 5 },
          "particles": {
            "color": "rgba(220,230,245, 0.2-0.45)",
            "size": "1.5-4px radius circles",
            "velocity": "drift with wind + gentle downward (25-60px/s)",
            "lifetime": "4-7 seconds",
            "note": "Mixed rain and snow — transitional arctic weather"
          }
        },
        "wind": {
          "0s": { "speed": 2 },
          "10s": { "speed": 5 },
          "visualIndicators": [
            "rain angle increases",
            "cloud speed increases",
            "operator lean increases",
            "occasional horizontal speed streaks (at wind>3)"
          ]
        },
        "fog": {
          "0s": { "opacity": 0 },
          "10s": { "opacity": 0.08 },
          "renderAs": "full-screen semi-transparent fill rgba(160,170,185, fog_opacity*0.4)"
        },
        "temperature": {
          "display": "bottom-left HUD box",
          "0s": "❄ -15°C",
          "10s": "❄ -25°C",
          "animation": "number ticks down smoothly"
        },
        "windSpeed": {
          "display": "next to temperature",
          "0s": "💨 40 km/h",
          "10s": "💨 80 km/h"
        }
      },

      "darkness": {
        "0s": 0.15,
        "10s": 0.3,
        "renderAs": "full-screen rgba(5,5,15, darkness*0.6)",
        "vignette": {
          "visible_from": "darkness > 0.2",
          "type": "radial gradient — transparent center, dark edges",
          "edge_opacity": "darkness * 0.3"
        }
      },

      "frost_overlay": {
        "opacity": "0.1 → 0.25 over segment",
        "renderAs": "CSS radial-gradient: transparent center 55%, rgba(180,210,240,0.35) at 85%, rgba(160,200,230,0.6) at 100%",
        "note": "Frost creeping in from edges of screen — cinematic cold effect"
      },

      "operator": {
        "movement": {
          "startX": "28% screen",
          "endX": "48% screen",
          "speed": "0.02 per second (slow — fighting wind)",
          "direction": "facing right (toward storage)"
        },
        "walkAnimation": {
          "legSwing": "sin(time*8) * 12px * scale, dampened by struggle",
          "armSwing": "opposite phase to legs, dampened by struggle",
          "bodyBob": "sin(time*16) * 3px — vertical bouncing",
          "note": "Animation is LABORED — shorter stride, heavier steps"
        },
        "struggle": {
          "0s": 1.0,
          "10s": 1.8,
          "effects": [
            "body leans INTO wind direction (rotate transform)",
            "step length decreases",
            "arm swing decreases",
            "head ducks down"
          ]
        },
        "shiver": {
          "0s": 0.3,
          "10s": 0.7,
          "renderAs": "high-frequency lateral oscillation: sin(time*25)*shiver_value"
        },
        "stumble": {
          "timestamp": "6.5s",
          "duration": 0.8,
          "animation": "sinusoidal vertical wobble at 15Hz, amplitude 6px",
          "audio": "whoosh + grunt sounds",
          "screenShake": 0.4,
          "note": "Wind gust nearly knocks them over"
        },
        "expression": "worried — furrowed brows, slight frown",
        "coldBreath": {
          "emitRate": "on sine wave peaks (sin(time*2) > 0.8)",
          "particles": {
            "origin": "mouth position",
            "color": "rgba(200,210,220,0.15)",
            "type": "smoke",
            "size": "3-5px",
            "velocity": "drift with wind, slight upward",
            "lifetime": "0.8s"
          }
        }
      },

      "complications": {
        "1.0s": {
          "add": "Storm system approaching rapidly",
          "display": "top-right panel, slides in from right",
          "style": "dark red background with warning border"
        },
        "6.5s": {
          "add": "Wind speed: 80+ km/h",
          "note": "Added when stumble occurs"
        }
      },

      "text_overlays": {
        "0.0_to_3.0": {
          "mainMessage": "⛈ Weather deteriorating…",
          "subMessage": "Temperature dropping. Storm arriving faster than forecast."
        },
        "3.0_to_6.0": {
          "mainMessage": "Fighting through 80km/h winds…",
          "subMessage": "Every step is a battle. Visibility dropping."
        },
        "6.5_to_10.0": {
          "mainMessage": "Nearly blown off feet!",
          "subMessage": "200 meters has never felt so far."
        }
      },

      "hud": {
        "timer": { "value": "counting at 6x real speed — shows ~5:00 to ~12:00 in-world minutes" },
        "lossCounter": {
          "0s": "$15,000",
          "10s": "$45,000",
          "increment": "smooth counter animation",
          "lossFlashes": [
            { "timestamp": "2.0s", "text": "-$15,000" },
            { "timestamp": "7.0s", "text": "-$10,000" }
          ]
        }
      },

      "audio": {
        "continuous": {
          "wind": "howling wind, volume increases from 4% to 8% over segment",
          "rain": "rain patter, increasing intensity",
          "music": "dark ambient drone, D minor, building tension"
        },
        "6.5s": {
          "whoosh": "sharp wind gust — noise burst 0.4s",
          "grunt": "operator grunt — low sawtooth 130Hz 0.2s"
        },
        "8.5s": {
          "thunderFar": "distant rumble — sawtooth 55Hz 1.2s, noise 0.03 volume"
        }
      },

      "screenEffects": {
        "6.5s": { "screenShake": 0.4, "duration": "0.5s" },
        "8.5s": { "subtleFlash": "lightning in distance — brief 40ms white flash at 10% opacity" }
      }
    },

    {
      "id": 5,
      "label": "SEGMENT 5 — SCENARIO B: ARRIVAL AT STORAGE + SEARCH BEGINS + PARTS 1 & 2 LOST",
      "timeRange": "00:40 – 00:50",
      "startFrame": 1200,
      "endFrame": 1500,
      "duration": 10,

      "narrative": "The operator finally reaches the storage unit, exhausted and freezing. A lightning strike illuminates the scene. They begin desperately searching through parts. Part 1 is examined but RIPPED FROM THEIR HANDS by a wind gust — lost in the snow. Part 2 is grabbed but DROPS AND SHATTERS on the frozen ground. Two parts lost. Panic sets in. Loss counter surges past $80,000.",

      "background": {
        "sky": "dark storm — #1a2030 top, #3a4050 bottom",
        "darkness": "0.35 → 0.50",
        "clouds": "dark (80% darkened), moving fast at 50px/s",
        "ground": "darkened, slight snow coverage (opacity 0.2)"
      },

      "weather": {
        "rain": { "rate": "14 → 16, heavy diagonal rain" },
        "wind": { "speed": "5.5 → 6.5" },
        "snow": { "rate": "5 → 6, mixing with rain" },
        "fog": { "opacity": "0.1 → 0.18" },
        "temperature": "❄ -28°C → -30°C",
        "windSpeed": "💨 90 → 100 km/h"
      },

      "camera": {
        "0.0_to_2.0": { "type": "medium_shot", "focus": "operator arriving at storage", "zoom": 1.05 },
        "2.0": { "type": "snap_to", "focus": "storage unit shelves — close up on parts", "zoom": 1.2 },
        "2.0_to_5.0": { "type": "slow_pan_across_shelves", "note": "Camera follows operator's hand across parts" },
        "5.5": { "type": "snap_shake", "intensity": 0.5, "note": "Part 1 blown away" },
        "8.0": { "type": "snap_shake", "intensity": 0.7, "note": "Part 2 shatters" }
      },

      "operator": {
        "0.0_to_2.0": {
          "position": "arriving at x=70%",
          "pose": "walk_exhausted — slower, heavier steps",
          "struggle": 1.5,
          "expression": "relief mixed with exhaustion"
        },
        "2.0_to_5.0": {
          "pose": "reach",
          "direction": "facing left (toward shelves)",
          "examPart": 0,
          "action_sequence": [
            { "time": "2.0s", "action": "leans toward shelf, reaches for Part 1" },
            { "time": "2.8s", "action": "picks up Part 1, holds it up to examine" },
            { "time": "3.5s", "action": "squinting in darkness, turning part in hands" },
            { "time": "4.2s", "action": "head shake — wrong part" },
            { "time": "4.8s", "action": "WIND GUST — part RIPPED from hands!" }
          ],
          "holdPart_2.8_to_4.8": { "visible": true, "color": "#8899aa" }
        },
        "4.8_to_5.5": {
          "pose": "frustrated",
          "arms": "thrown up in frustration",
          "expression": "panicked — eyes wide, mouth open",
          "exclamation": "visible frustration animation"
        },
        "5.5_to_8.0": {
          "pose": "reach",
          "examPart": 1,
          "action_sequence": [
            { "time": "5.5s", "action": "reaches for Part 2 with shaking hands" },
            { "time": "6.3s", "action": "picks up Part 2 — it's covered in ice" },
            { "time": "6.8s", "action": "ice makes it slippery — struggling to grip" },
            { "time": "7.2s", "action": "fingers too numb — part SLIPS" },
            { "time": "7.5s", "action": "Part 2 CRASHES to frozen ground and SHATTERS!" }
          ]
        },
        "8.0_to_10.0": {
          "pose": "frustrated",
          "expression": "PANIC — eyes huge, sweat drops visible",
          "struggle": 2.0,
          "shiver": 1.0,
          "note": "Two parts lost. Two remaining. Desperation."
        }
      },

      "part_events": {
        "4.8s_part1_blown": {
          "animation": "part flies off screen right, accelerating with wind",
          "trajectory": "parabolic arc from hand position to off-screen right",
          "duration": "0.5s",
          "audio": "whoosh + crack",
          "screenShake": 0.5,
          "complication_added": "Wind BLEW Part 1 off the shelf!",
          "table_parts_0_state": "blown"
        },
        "7.5s_part2_shattered": {
          "animation": "part drops straight down from hand, hits ground",
          "impact_particles": {
            "count": 15,
            "colors": ["#99887a", "#bbaa99", "#776655"],
            "velocity": "radial burst outward + upward",
            "size": "2-4px",
            "type": "spark",
            "gravity": 200,
            "lifetime": "0.3-0.5s"
          },
          "audio": ["shatter (3000Hz+1500Hz+800Hz square cascading 0.08-0.15s)", "crash (80Hz sawtooth 0.4s)"],
          "screenShake": 0.7,
          "redFlash": { "opacity": 0.15, "duration": "150ms" },
          "alert_popup": {
            "title": "PART DESTROYED",
            "subtitle": "Coupling B shattered on impact!",
            "duration": "3 seconds"
          },
          "complication_added": "Part 2 SHATTERED – dropped on frozen ground!",
          "table_parts_1_state": "broken",
          "lossFlash": "-$15,000"
        }
      },

      "lightning": {
        "0.5s": {
          "type": "CLOSE STRIKE",
          "bolt": {
            "segments": 10,
            "start": "random x 20-80%, y=0",
            "end": "ground level",
            "zigzag": "random ±50px per segment",
            "branches": "every 3rd segment, random direction 60px",
            "color": "rgba(220,230,255, flash_intensity)",
            "lineWidth": 2.5,
            "glow": { "blur": 20, "color": "#aaddff" }
          },
          "flash": { "intensity": 1.0, "decay": "multiply by 0.88 per frame" },
          "screenFlash": "80ms white at 35% opacity",
          "audio": "LOUD thunder — 45Hz sawtooth 2s + noise burst",
          "screenShake": 0.6
        }
      },

      "text_overlays": {
        "0.0_to_2.0": { "main": "Finally reached spare parts storage…", "sub": "Covered in snow. Visibility near zero." },
        "2.0_to_4.5": { "main": "Examining Part 1: Valve A", "sub": "Trying to identify in near-darkness…" },
        "4.8_to_5.5": { "main": "💨 Part 1 ripped away by wind gust!", "sub": "Lost somewhere in the snow. Unrecoverable." },
        "5.5_to_7.5": { "main": "Trying Part 2: Coupling B", "sub": "Fingers numb — can barely grip…" },
        "7.5_to_10.0": { "main": "💥 Part 2 DESTROYED!", "sub": "Shattered on frozen ground. Two parts lost." }
      },

      "hud": {
        "timer": "counting — shows ~16:00 → ~22:00 in-world",
        "lossCounter": {
          "0s": "$55,000",
          "5s": "$70,000",
          "8s": "$85,000",
          "10s": "$90,000",
          "lossFlashes": [
            { "time": "4.8s", "text": "-$10,000" },
            { "time": "7.5s", "text": "-$15,000" }
          ]
        }
      },

      "audio": {
        "continuous": {
          "wind": "howling 8% volume, with gusts at 4.8s (sharp whoosh)",
          "rain": "heavy patter 6%",
          "music": "dark minor key tension, building dissonance"
        },
        "0.5s": "thunder_loud",
        "4.8s": ["whoosh", "crack", "grunt"],
        "7.5s": ["shatter", "crash"],
        "8.5s": "operator frustrated sigh — low tone"
      }
    },

    {
      "id": 6,
      "label": "SEGMENT 6 — SCENARIO B: PARTS 3 & 4 + FROZEN PART STRUGGLE",
      "timeRange": "00:50 – 01:00",
      "startFrame": 1500,
      "endFrame": 1800,
      "duration": 10,

      "narrative": "Part 3 is wrong specification — useless. ONE PART LEFT. Part 4 — the Impeller X — is encased in ice, frozen to the shelf. The operator spends agonizing seconds chipping ice with numb fingers, progress shown on screen. Ice cracking sounds. Finally the part breaks free. Now comes the worst part: getting back through the full-fury blizzard. Loss counter passes $110,000.",

      "background": {
        "darkness": "0.50 → 0.60",
        "sky": "very dark storm #0f1520 → near black"
      },

      "weather": {
        "rain": { "rate": "16 → 18, torrential" },
        "wind": { "speed": "6.5 → 7.5" },
        "snow": { "rate": "6 → 8, blizzard conditions" },
        "fog": { "opacity": "0.18 → 0.25" },
        "temperature": "❄ -30°C → -34°C",
        "windSpeed": "💨 100 → 115 km/h"
      },

      "operator": {
        "0.0_to_3.0": {
          "part3_search": {
            "pose": "reach then holdUp",
            "examPart": 2,
            "sequence": [
              { "0.0s": "reaches for Part 3 on shelf" },
              { "0.8s": "picks up, holds to face — squinting" },
              { "1.5s": "turns part, checking markings" },
              { "2.2s": "realization — WRONG SPEC" },
              { "2.5s": "puts back, shakes head" }
            ],
            "holdPart_0.8_to_2.5": { "visible": true, "color": "#7a8899" },
            "expression": "confusion → frustration",
            "audio_2.2s": "installFail sound — low buzz"
          }
        },
        "3.0_to_8.0": {
          "part4_frozen_struggle": {
            "pose": "reach",
            "examPart": 3,
            "narrative": "Found the right part — but it's FROZEN SOLID to the shelf!",
            "struggle_animation": {
              "type": "pulling/twisting motion — arms straining",
              "screenShake": "periodic 0.15 intensity at each pull attempt",
              "ice_crack_sfx": "every 1.5 seconds — crack sound",
              "progress_display": {
                "visible": true,
                "text": "Breaking ice… XX%",
                "progression": [
                  { "3.5s": "15%" },
                  { "4.5s": "35%" },
                  { "5.5s": "60%" },
                  { "6.5s": "80%" },
                  { "7.0s": "95%" },
                  { "7.5s": "100% — FREE!" }
                ]
              }
            },
            "7.5s_freed": {
              "audio": ["crack", "crack (double)", "relieved grunt"],
              "animation": "part comes loose — operator stumbles back slightly",
              "holdPart": true,
              "partColor": "#00bbee",
              "pose_change": "holdUp — inspecting freed part",
              "complication_cleared_visual": "brief green flash on part"
            }
          }
        },
        "8.0_to_10.0": {
          "pose": "stand",
          "direction": "turns left — looking back toward equipment 200m away",
          "expression": "dread — realizes the walk back through peak storm",
          "holdPart": true,
          "struggle": 2.0,
          "shiver": 1.2
        }
      },

      "text_overlays": {
        "0.0_to_2.5": { "main": "Part 3: Flange C – checking specification…", "sub": "Squinting in darkness at part markings…" },
        "2.5_to_3.0": { "main": "Part 3: WRONG SPECIFICATION", "sub": "Diameter mismatch. Cannot risk wrong part." },
        "3.0_to_7.5": { "main": "Part 4: Impeller X – ENCASED IN ICE", "sub": "Breaking ice with numb hands… [progress%]" },
        "7.5_to_8.5": { "main": "✓ Part freed from ice!", "sub": "Now the hardest part: getting back through the storm." },
        "8.5_to_10.0": { "main": "Must get back to equipment NOW!", "sub": "Storm at maximum. Equipment taking damage every second." }
      },

      "complications": {
        "2.5s": "Part 3: Wrong spec – cannot use",
        "3.0s": "Correct part frozen to shelf!"
      },

      "hud": {
        "timer": "~22:00 → ~30:00 in-world",
        "lossCounter": {
          "0s": "$90,000",
          "3s": "$100,000",
          "8s": "$110,000",
          "lossFlashes": [
            { "time": "2.5s", "text": "-$10,000" },
            { "time": "7.5s", "text": "-$10,000" }
          ]
        }
      },

      "audio": {
        "continuous": "wind howling 10%, rain heavy, dark music building",
        "crackingSounds": "at 3.5s, 4.5s, 5.5s, 6.5s, 7.5s — increasing intensity",
        "2.5s": "installFail — buzz/disappointment",
        "7.5s": ["crack (loud)", "relieved grunt"]
      }
    },

    {
      "id": 7,
      "label": "SEGMENT 7 — SCENARIO B: NIGHTMARE WALK BACK + EQUIPMENT CASCADE FAILURE",
      "timeRange": "01:00 – 01:10",
      "startFrame": 1800,
      "endFrame": 2100,
      "duration": 10,

      "narrative": "The most intense segment. Full blizzard fury. The operator fights through 120+ km/h winds carrying the precious part. Lightning strikes. They stumble badly. Meanwhile, the equipment — visible in the distance — starts suffering SECONDARY CASCADE DAMAGE from extended downtime. Smoke pours from it. New cracks appear. Alert popup screams CASCADE FAILURE. The operator is battered, exhausted, barely standing. Loss counter rockets past $150,000.",

      "background": {
        "darkness": "0.60 → 0.70 — near nighttime darkness",
        "sky": "almost black with storm clouds",
        "visibility": "severely impaired — fog + rain + snow"
      },

      "weather": {
        "rain": { "rate": "20+, TORRENTIAL — screen is streaked with rain lines" },
        "wind": { "speed": "8+, HURRICANE FORCE" },
        "snow": { "rate": "9+, FULL BLIZZARD" },
        "fog": { "opacity": "0.25+" },
        "temperature": "❄ -35°C → -38°C",
        "windSpeed": "💨 120+ km/h",
        "windStreaks": {
          "visible": true,
          "count": "2-3 per second",
          "description": "long horizontal rain-type particles moving at 500+px/s across screen",
          "opacity": 0.12
        }
      },

      "frost_overlay": {
        "opacity": "0.5 → 0.65",
        "note": "Screen edges significantly frosted — claustrophobic feel"
      },

      "camera": {
        "overall": "UNSTABLE — continuous low-level shake from wind force",
        "baseShake": 0.3,
        "0.0_to_3.0": { "type": "tracking_shot", "follows": "operator walking left", "zoom": 1.05 },
        "3.5": { "type": "snap_shake", "intensity": 1.5, "note": "Stumble moment — HEAVY shake" },
        "5.0": { "type": "snap_shake", "intensity": 1.2, "note": "Lightning strike" },
        "6.0_to_8.0": { "type": "cut_to", "focus": "equipment in distance", "zoom": 1.15, "note": "Show equipment taking damage" },
        "8.0_to_10.0": { "type": "wide", "zoom": 0.95, "note": "Show full scene — operator struggling, equipment smoking" }
      },

      "operator": {
        "movement": {
          "startX": "68%",
          "endX": "42%",
          "note": "Only covers half the return distance — storm is that bad"
        },
        "struggle": "2.5 → 3.0 (maximum)",
        "shiver": "1.5 → 2.0",
        "exhaustion": 0.8,
        "windLean": "body tilted 12-15 degrees into wind — extreme lean",
        "walkAnimation": {
          "speed": "VERY SLOW — step frequency reduced 50%",
          "stride": "SHORT — dampened by struggle factor",
          "bobIntensity": "heavy, labored"
        },
        "stumble_3.5s": {
          "duration": 1.5,
          "amplitude": "12px vertical wobble",
          "screenShake": 1.5,
          "audio": ["crash/thud", "grunt", "whoosh"],
          "complication": "Operator nearly FELL – risk of part damage"
        },
        "flinch_5.0s": {
          "reaction": "ducks head, hunches shoulders for 0.5s",
          "note": "Flinching from nearby lightning strike"
        },
        "holdPart": true,
        "partColor": "#00bbee",
        "expression": "panicked — wide eyes (2.5px), open mouth, sweat drops on both sides",
        "coldBreath": "every 1.5 seconds — larger clouds than before, drift fast with wind",
        "pose": "stand (walking with held part visible against body)"
      },

      "equipment": {
        "6.0s_cascade_damage": {
          "trigger": "shown while camera cuts to equipment",
          "crack_level": "increases from 1 to 3 (maximum)",
          "new_cracks": [
            "crack line 2: 75% top → 65% at 30% → 72% at 50%",
            "crack line 3: 10% at 50% → 25% at 65% → 12% at 85%",
            "crack line 4: 50% at 60% → 60% at 75% → 45% at 90%"
          ],
          "smoke": "HEAVY — 1.5 particles/second, larger clouds",
          "sparks": "electrical arcs — 3 spark particles every 0.3 seconds",
          "status": "error — flashing aggressively",
          "display": "!! FAILURE !! blinking fast",
          "warningBeacon": "intense red pulse",
          "shake": "0.4-0.7 continuous (from internal damage + wind)",
          "audio": "creaking metal (120Hz sawtooth 0.6s) + (90Hz triangle 0.8s)"
        },
        "alert_popup_6.5s": {
          "title": "⚠ CASCADE FAILURE",
          "subtitle": "Extended downtime causing corrosion & thermal damage!",
          "style": "red background, white text, border glow",
          "duration": "3.5 seconds",
          "animation": "scale pop with bounce"
        }
      },

      "lightning": {
        "5.0s": {
          "type": "CLOSE_STRIKE — dramatic",
          "bolt": "procedural zigzag from top to ground, 12 segments",
          "branches": 3,
          "flash_intensity": 1.0,
          "thunder": "LOUD — immediate, no delay (close strike)",
          "screenShake": 1.2,
          "audio": ["thunder_loud (45Hz 2s + noise)", "wind_whoosh"]
        },
        "8.5s": {
          "type": "distant flash",
          "bolt": "smaller, right side of screen",
          "flash_intensity": 0.5,
          "thunder": "delayed 0.8s, quieter"
        }
      },

      "complications": {
        "0.5s": "Storm at MAXIMUM intensity",
        "3.5s": "Operator nearly FELL – risk of part damage",
        "6.5s": "SECONDARY EQUIPMENT DAMAGE detected!"
      },

      "text_overlays": {
        "0.0_to_3.0": { "main": "Fighting back through blizzard conditions…", "sub": "Visibility: near ZERO. Wind: 120+ km/h" },
        "3.5_to_5.0": { "main": "NEARLY KNOCKED DOWN BY WIND GUST!", "sub": "Scrambling to keep hold of the part…" },
        "6.0_to_8.0": { "main": "⚠️ Equipment suffering secondary damage!", "sub": "Corrosion + thermal stress from extended exposure" },
        "8.0_to_10.0": { "main": "Almost there… but at what cost?", "sub": "Equipment has been down for nearly an hour" }
      },

      "hud": {
        "timer": "~32:00 → ~55:00 in-world (time acceleration)",
        "lossCounter": {
          "0s": "$115,000",
          "5s": "$130,000",
          "7s": "$150,000",
          "10s": "$165,000",
          "lossFlashes": [
            { "time": "3.5s", "text": "-$15,000" },
            { "time": "6.5s", "text": "-$20,000" }
          ]
        }
      },

      "audio": {
        "continuous": {
          "wind": "DEAFENING howl — 14% volume, continuous",
          "rain": "hammering patter — 8%",
          "music": "maximum tension — dissonant strings, low brass hits on complications"
        },
        "3.5s": ["crash", "grunt", "whoosh"],
        "5.0s": "thunder_LOUD",
        "6.5s": ["creak (metal stress)", "alarm beep"],
        "8.5s": "thunder_distant"
      }
    },

    {
      "id": 8,
      "label": "SEGMENT 8 — SCENARIO B: FAILED FIRST INSTALL + BARELY SUCCEED + AFTERMATH",
      "timeRange": "01:10 – 01:20",
      "startFrame": 2100,
      "endFrame": 2400,
      "duration": 10,

      "narrative": "The operator reaches the equipment, completely battered. First installation attempt FAILS — hands too frozen, part misaligned. Second attempt barely succeeds. Equipment limps to 60% capacity with grinding gears. Then the devastating damage assessment: line items appear one by one totaling $355,000+ in losses. The operator stands defeated in the raging storm. Everything that could go wrong did.",

      "background": {
        "darkness": "0.65 — sustained darkness",
        "weather": "still raging but slightly less intense (storm passing peak)",
        "note": "Dark, moody, defeated atmosphere"
      },

      "weather": {
        "rain": { "rate": "decreasing 18 → 12" },
        "wind": { "speed": "decreasing 7 → 5" },
        "snow": { "rate": "8 → 6" },
        "note": "Storm slightly abating but still hostile"
      },

      "operator": {
        "arrival_0.0_to_1.5": {
          "position": "arriving at x=30%",
          "pose": "walk_exhausted",
          "struggle": 2.5,
          "exhaustion": 1.0,
          "shiver": 2.0,
          "expression": "desperate exhaustion",
          "holdPart": true
        },
        "install_attempt_1": {
          "timeRange": "1.5s – 3.5s",
          "pose": "install",
          "holdPart_released": "1.5s",
          "animation": "arms forward, working on equipment front panel",
          "3.0s_FAILURE": {
            "audio": ["installFail (buzz)", "grunt"],
            "screenShake": 0.3,
            "redFlash": "100ms",
            "alert": { "title": "INSTALLATION FAILED", "subtitle": "Part slipped – misalignment!", "duration": "2.5s" },
            "complication": "First installation attempt FAILED!",
            "operator_reaction": "frustrated — head drops, arms shake",
            "lossFlash": "-$15,000"
          }
        },
        "install_attempt_2": {
          "timeRange": "3.5s – 5.5s",
          "pose": "install",
          "narrative": "Trying again with last ounce of strength",
          "5.0s_SUCCESS": {
            "barely": true,
            "audio": ["clang (weak)", "sad boop (250Hz 0.8s — deflated)"],
            "equipment_status": "warn (NOT ok — compromised)",
            "gear": "stuttering rotation — sin wave speed variation 0.2-0.4 rad/s",
            "capacity": 60,
            "crack_level": "remains at 3",
            "smoke": "continues at 0.5/sec",
            "sparks": "occasional — 0.3/sec"
          }
        },
        "aftermath_5.5_to_10.0": {
          "pose": "defeated",
          "arms": "hanging limply at sides",
          "head": "bowed",
          "expression": "defeat — no smile, eyes downcast",
          "struggle": 2.0,
          "exhaustion": 1.0,
          "note": "Standing motionless in the rain, looking at the damage"
        }
      },

      "damageAssessment": {
        "start": "6.0s",
        "sequence": [
          {
            "timestamp": "6.5s",
            "text": "Lost production (70 min): -$150,000",
            "lossJump": 220000,
            "lossFlash": "-$150,000",
            "complication_add": "Lost production: $150,000",
            "audio": "low impact tone"
          },
          {
            "timestamp": "7.5s",
            "text": "Secondary equipment damage: -$100,000",
            "lossJump": 300000,
            "lossFlash": "-$100,000",
            "complication_add": "Secondary damage: $100,000",
            "audio": "deeper impact tone"
          },
          {
            "timestamp": "8.5s",
            "text": "Storm exposure corrosion: -$50,000",
            "lossJump": 340000,
            "lossFlash": "-$50,000",
            "complication_add": "Corrosion damage: $50,000"
          },
          {
            "timestamp": "9.2s",
            "text": "Broken spare parts: -$15,000",
            "lossJump": 355000,
            "lossFlash": "-$15,000",
            "complication_add": "Broken parts: $15,000",
            "alert": {
              "title": "TOTAL LOSSES",
              "subtitle": "$355,000+",
              "style": "LARGE red alert, 5 second duration",
              "animation": "dramatic scale from 0.5 to 1.0"
            }
          }
        ]
      },

      "text_overlays": {
        "0.0_to_1.5": { "main": "Finally reached equipment…", "sub": "Completely exhausted. Fingers frozen." },
        "1.5_to_3.0": { "main": "Attempting installation…", "sub": "Hands shaking. Part alignment critical." },
        "3.0_to_3.5": { "main": "❌ Installation FAILED!", "sub": "Part slipped! Must try again…" },
        "3.5_to_5.0": { "main": "Second attempt… this HAS to work…", "sub": "Careful… careful…" },
        "5.0_to_6.0": { "main": "Equipment barely operational – 60% capacity", "sub": "Part and equipment both damaged." },
        "6.0_to_8.5": { "main": "DAMAGE ASSESSMENT", "sub": "Calculating total impact…" },
        "9.0_to_10.0": { "main": "One storm. 70 minutes. $355,000+ in damages.", "sub": "Equipment may never fully recover." }
      },

      "equipment": {
        "capacityBar": {
          "visible_from": "5.0s",
          "percentage": 60,
          "color": "#dd2222",
          "label": "60% CAPACITY"
        }
      },

      "hud": {
        "timer": {
          "freezes_at": "70:00 in-world",
          "display": "01:10",
          "color": "red with ✗ symbol"
        },
        "lossCounter": {
          "dramatic_climb": "see damageAssessment sequence",
          "final_value": "$355,000+"
        }
      },

      "audio": {
        "5.0s": "sadBoop — 200Hz+150Hz sine, 0.8s — deflating, weak",
        "damageItems": "low impact tones increasing in bass weight",
        "music": "reaches emotional nadir — single sustained minor chord, fading",
        "wind": "still present but subsiding — 6% volume"
      }
    },

    {
      "id": 9,
      "label": "SEGMENT 9 — COMPARISON + CALL TO ACTION",
      "timeRange": "01:20 – 01:30",
      "startFrame": 2400,
      "endFrame": 2700,
      "duration": 10,

      "narrative": "Fade to black. Then the side-by-side comparison appears: Scenario A vs Scenario B with every metric contrasted. Green vs Red. $0 vs $355,000+. 15 seconds vs 70+ minutes. The contrast is devastating. Then the final CTA: AddManuChain branding, tagline, and call to action. The message is undeniable.",

      "transition": {
        "0.0_to_1.5": {
          "type": "fade_to_black",
          "duration": "1.2s",
          "all_elements_fade": "HUD, messages, weather, scene — everything",
          "audio": "all sound fades to silence"
        }
      },

      "comparison_screen": {
        "appears_at": "1.5s",
        "background": "radial gradient from #0a1628 (center) to #000 (edges)",
        "fadeIn": "0.8s",

        "title": {
          "text": "One Decision. Two Outcomes.",
          "font": "38px weight 800",
          "color": "#ffffff",
          "position": "top center with 30px padding",
          "animation": "fade in + slight scale from 0.95 to 1.0"
        },

        "cards": {
          "layout": "two cards side by side, 45% width each, centered",
          "gap": "30px",
          "animation": "slide in from sides — left card from left, right from right, 0.5s ease-out",

          "left_card_scenarioA": {
            "style": {
              "background": "linear-gradient(135deg, rgba(0,200,100,0.1), rgba(13,217,255,0.06))",
              "border": "1px solid rgba(0,255,150,0.2)",
              "borderRadius": "14px",
              "padding": "26px"
            },
            "header": "⚡ SCENARIO A — On-Demand Parts",
            "metrics": [
              { "icon": "⏱", "label": "Downtime", "value": "15 seconds", "valueColor": "#00ff66" },
              { "icon": "💰", "label": "Production Loss", "value": "$0", "valueColor": "#00ff66" },
              { "icon": "📦", "label": "Inventory", "value": "Digital (KB)", "valueColor": "#00ff66" },
              { "icon": "🛡", "label": "Weather Risk", "value": "None", "valueColor": "#00ff66" },
              { "icon": "🔧", "label": "Equipment", "value": "100%", "valueColor": "#00ff66" },
              { "icon": "✅", "label": "Result", "value": "MISSION SUCCESS", "valueColor": "#00ff66" }
            ],
            "metricAnimation": "each row fades in 0.2s apart (staggered)"
          },

          "right_card_scenarioB": {
            "style": {
              "background": "linear-gradient(135deg, rgba(200,0,0,0.1), rgba(100,0,0,0.06))",
              "border": "1px solid rgba(255,50,50,0.2)",
              "borderRadius": "14px",
              "padding": "26px"
            },
            "header": "📦 SCENARIO B — Traditional Inventory",
            "metrics": [
              { "icon": "⏱", "label": "Downtime", "value": "70+ minutes", "valueColor": "#ff4444" },
              { "icon": "💰", "label": "Production Loss", "value": "$355,000+", "valueColor": "#ff4444" },
              { "icon": "📦", "label": "Inventory", "value": "Physical Warehouse", "valueColor": "#ff4444" },
              { "icon": "⚠️", "label": "Weather Risk", "value": "Critical", "valueColor": "#ff4444" },
              { "icon": "🔧", "label": "Equipment", "value": "60% (Damaged)", "valueColor": "#ff4444" },
              { "icon": "❌", "label": "Result", "value": "CATASTROPHIC FAILURE", "valueColor": "#ff4444" }
            ],
            "metricAnimation": "same stagger as left card"
          }
        },

        "bottomMessage": {
          "text": "EVERY DELAY IN REMOTE OPERATIONS = CATASTROPHIC LOSS",
          "font": "20px weight 700",
          "color": "#ff9966",
          "animation": "fade in at 4.0s, pulse glow"
        },

        "duration_visible": "1.5s to 6.5s (5 seconds)"
      },

      "cta_screen": {
        "appears_at": "6.5s",
        "transition": "comparison fades out, CTA fades in over 0.8s",
        "background": "same radial gradient",

        "headline": {
          "text": "In remote operations,\nevery second counts.",
          "font": "42px weight 800",
          "color": "#ffffff",
          "lineHeight": 1.2,
          "position": "upper center"
        },

        "subtext": {
          "text": "From $355,000+ in losses to $0 downtime.\nDigital parts. On-demand printing. Mission-critical reliability.",
          "font": "17px",
          "color": "#99aabb",
          "highlights": [
            { "text": "$355,000+ in losses", "color": "#0dd9ff", "weight": 700 },
            { "text": "$0 downtime", "color": "#0dd9ff", "weight": 700 }
          ],
          "lineHeight": 1.5
        },

        "brand": {
          "text": "AddManuChain",
          "font": "28px weight 900, letter-spacing 3px",
          "style": "linear-gradient(135deg, #0dd9ff, #00ff88) background-clip text",
          "animation": "subtle glow pulse"
        },

        "contact": {
          "text": "Let's talk about your remote operations.",
          "font": "14px",
          "color": "#6699bb"
        },

        "replayButton": {
          "text": "↻ REPLAY DEMO",
          "style": "outlined button, white text, semi-transparent background",
          "hoverEffect": "cyan border glow"
        }
      },

      "audio": {
        "1.5s": "subtle ambient pad fades in — C major, hopeful",
        "3.0s": "soft piano note — single chord",
        "6.5s": "gentle ascending synth — resolve, hope, clarity",
        "note": "Audio shifts from tension to resolution — emotional release"
      }
    }
  ],

  "globalAssets": {
    "colorPalette": {
      "scenarioA_primary": "#0dd9ff",
      "scenarioA_secondary": "#00ff88",
      "scenarioB_danger": "#ff3333",
      "scenarioB_warning": "#ffaa00",
      "equipment_body": "#1c4466",
      "equipment_dark": "#102a3e",
      "text_primary": "#ffffff",
      "text_secondary": "#cccccc",
      "text_muted": "#888888",
      "sky_clear": "#5599cc",
      "sky_storm": "#0a0a18",
      "ground_normal": "#d8e8d0",
      "ground_dark": "#2a2a30",
      "loss_red": "#ff4444",
      "success_green": "#00ff66",
      "part_cyan": "#00ccff",
      "part_gray": "#888888"
    },

    "audioDesign": {
      "scenarioA_music": "bright synth pad, C major, tempo 100bpm, volume 15-20%",
      "scenarioB_music": "dark ambient drone, D minor, tempo 60bpm, dissonant, volume 10-18%, builds in intensity",
      "transition_music": "silence → resolve",
      "cta_music": "hopeful ambient, gentle, volume 12%",
      "wind_continuous": "noise generator with lowpass filter at 400Hz",
      "rain_continuous": "noise at varying volume levels",
      "all_sfx_use": "Web Audio API oscillators and noise buffers"
    },

    "particleTypes": {
      "rain": { "render": "line from position to position+velocity*0.02", "lineWidth": 1.2 },
      "snow": { "render": "circle with radius=size", "fade": "opacity follows life ratio" },
      "spark": { "render": "square size*opacity", "gravity": true, "fade": "opacity follows life ratio" },
      "smoke": { "render": "circle growing over lifetime (1.5x)", "fade": "opacity follows life ratio" },
      "dot": { "render": "circle shrinking over lifetime", "fade": "opacity follows life ratio" },
      "confetti": { "render": "rectangle with rotation", "gravity": true }
    },

    "emotionalArc": {
      "00_to_10": "confidence → shock → calm resolution",
      "10_to_20": "satisfaction → triumph → celebration",
      "20_to_30": "reset → dread → oh no",
      "30_to_40": "struggle → fear → desperation",
      "40_to_50": "hope → loss → loss → PANIC",
      "50_to_60": "determination → frustration → relief → dread",
      "60_to_70": "terror → exhaustion → cascade horror",
      "70_to_80": "last effort → failure → barely succeed → devastation",
      "80_to_90": "clarity → contrast → resolve → call to action"
    }
  }
}