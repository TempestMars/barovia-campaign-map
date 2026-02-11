import os

# SVG templates for different location types
icons = {
    'castle': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="16" y="28" width="32" height="32" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="12" y="20" width="8" height="12" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="44" y="20" width="8" height="12" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="26" y="14" width="12" height="18" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="20,28 28,20 36,20 44,28" fill="#6a4a3a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="28" y="44" width="8" height="16" fill="#2a2a2a" stroke="#c9a961" stroke-width="1"/>
        <rect x="14" y="18" width="4" height="4" fill="#c9a961"/>
        <rect x="46" y="18" width="4" height="4" fill="#c9a961"/>
        <rect x="28" y="12" width="4" height="4" fill="#c9a961"/>
    </svg>''',
    
    'church': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="20" y="30" width="24" height="28" fill="#6a5a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="32,8 20,20 44,20" fill="#8a6a5a" stroke="#c9a961" stroke-width="2"/>
        <rect x="28" y="4" width="8" height="16" fill="#6a5a4a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="30" y="2" width="4" height="4" fill="#c9a961"/>
        <rect x="26" y="44" width="12" height="14" fill="#3a2a1a" stroke="#c9a961" stroke-width="1"/>
        <circle cx="32" cy="28" r="3" fill="#ffd700"/>
    </svg>''',
    
    'village': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="10" y="32" width="16" height="20" fill="#6a5a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="18,32 10,20 26,20" fill="#8a4a3a" stroke="#c9a961" stroke-width="2"/>
        <rect x="38" y="36" width="14" height="16" fill="#6a5a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="45,36 38,26 52,26" fill="#8a4a3a" stroke="#c9a961" stroke-width="2"/>
        <rect x="14" y="42" width="6" height="10" fill="#3a2a1a"/>
        <rect x="42" y="44" width="6" height="8" fill="#3a2a1a"/>
        <rect x="22" y="36" width="4" height="4" fill="#ffd700"/>
        <rect x="46" y="38" width="3" height="3" fill="#ffd700"/>
    </svg>''',
    
    'windmill': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <polygon points="32,50 26,58 38,58" fill="#8a6a5a" stroke="#c9a961" stroke-width="2"/>
        <rect x="28" y="30" width="8" height="20" fill="#8a6a5a" stroke="#c9a961" stroke-width="2"/>
        <circle cx="32" cy="28" r="4" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <line x1="32" y1="28" x2="32" y2="14" stroke="#6a4a3a" stroke-width="3"/>
        <line x1="32" y1="28" x2="46" y2="28" stroke="#6a4a3a" stroke-width="3"/>
        <line x1="32" y1="28" x2="18" y2="28" stroke="#6a4a3a" stroke-width="3"/>
        <line x1="32" y1="28" x2="32" y2="42" stroke="#6a4a3a" stroke-width="3"/>
        <polygon points="32,14 28,18 36,18" fill="#8a6a5a"/>
        <polygon points="46,28 42,24 42,32" fill="#8a6a5a"/>
    </svg>''',
    
    'tower': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="24" y="20" width="16" height="38" fill="#5a5a5a" stroke="#c9a961" stroke-width="2"/>
        <rect x="20" y="16" width="24" height="6" fill="#6a6a6a" stroke="#c9a961" stroke-width="2"/>
        <rect x="18" y="14" width="4" height="4" fill="#c9a961"/>
        <rect x="42" y="14" width="4" height="4" fill="#c9a961"/>
        <rect x="28" y="28" width="8" height="8" fill="#3a3a3a" stroke="#c9a961" stroke-width="1"/>
        <rect x="28" y="40" width="8" height="8" fill="#3a3a3a" stroke="#c9a961" stroke-width="1"/>
        <rect x="30" y="50" width="4" height="8" fill="#2a2a2a"/>
    </svg>''',
    
    'temple': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <polygon points="32,10 16,24 48,24" fill="#6a5a5a" stroke="#c9a961" stroke-width="2"/>
        <rect x="20" y="24" width="6" height="30" fill="#5a4a4a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="29" y="24" width="6" height="30" fill="#5a4a4a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="38" y="24" width="6" height="30" fill="#5a4a4a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="16" y="54" width="32" height="4" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="32,10 30,6 34,6" fill="#c9a961"/>
    </svg>''',
    
    'camp': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <polygon points="32,16 20,46 44,46" fill="#8a6a5a" stroke="#c9a961" stroke-width="2"/>
        <line x1="20" y1="46" x2="44" y2="46" stroke="#4a3a2a" stroke-width="3"/>
        <circle cx="32" cy="50" r="4" fill="#ff6600" stroke="#ff3300" stroke-width="1"/>
        <circle cx="32" cy="50" r="2" fill="#ffaa00"/>
        <line x1="28" y1="52" x2="24" y2="56" stroke="#6a4a3a" stroke-width="2"/>
        <line x1="36" y1="52" x2="40" y2="56" stroke="#6a4a3a" stroke-width="2"/>
    </svg>''',
    
    'gate': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="12" y="14" width="8" height="44" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="44" y="14" width="8" height="44" fill="#4a4a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="20" y="28" width="24" height="24" fill="#3a3a3a" stroke="#c9a961" stroke-width="2"/>
        <rect x="28" y="36" width="8" height="16" fill="#2a2a2a" stroke="#c9a961" stroke-width="1"/>
        <line x1="12" y1="28" x2="52" y2="28" stroke="#c9a961" stroke-width="2"/>
        <rect x="10" y="10" width="6" height="6" fill="#c9a961"/>
        <rect x="48" y="10" width="6" height="6" fill="#c9a961"/>
    </svg>''',
    
    'lake': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <ellipse cx="32" cy="36" rx="24" ry="18" fill="#4a7a9a" stroke="#6aa0c0" stroke-width="2"/>
        <ellipse cx="28" cy="32" rx="8" ry="6" fill="#6aa0c0" opacity="0.5"/>
        <ellipse cx="38" cy="36" rx="6" ry="4" fill="#6aa0c0" opacity="0.5"/>
        <path d="M 16,28 Q 20,24 24,28" stroke="#8ac0e0" stroke-width="2" fill="none"/>
        <path d="M 40,32 Q 44,28 48,32" stroke="#8ac0e0" stroke-width="2" fill="none"/>
    </svg>''',
    
    'bridge': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="8" y="28" width="48" height="8" fill="#6a5a4a" stroke="#c9a961" stroke-width="2"/>
        <rect x="12" y="36" width="4" height="16" fill="#5a4a3a" stroke="#c9a961" stroke-width="1"/>
        <rect x="28" y="36" width="4" height="16" fill="#5a4a3a" stroke="#c9a961" stroke-width="1"/>
        <rect x="44" y="36" width="4" height="16" fill="#5a4a3a" stroke="#c9a961" stroke-width="1"/>
        <path d="M 10,50 Q 32,56 54,50" stroke="#4a7a9a" stroke-width="3" fill="none"/>
    </svg>''',
    
    'winery': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="18" y="34" width="28" height="22" fill="#6a4a4a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="32,18 18,34 46,34" fill="#8a5a4a" stroke="#c9a961" stroke-width="2"/>
        <circle cx="26" cy="26" r="3" fill="#9a5a9a" stroke="#7a3a7a" stroke-width="1"/>
        <circle cx="32" cy="24" r="3" fill="#9a5a9a" stroke="#7a3a7a" stroke-width="1"/>
        <circle cx="38" cy="26" r="3" fill="#9a5a9a" stroke="#7a3a7a" stroke-width="1"/>
        <rect x="28" y="44" width="8" height="12" fill="#3a2a1a" stroke="#c9a961" stroke-width="1"/>
        <rect x="22" y="40" width="6" height="6" fill="#ffd700" stroke="#c9a961" stroke-width="0.5"/>
    </svg>''',
    
    'hill': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <path d="M 4,50 Q 16,20 32,28 Q 48,36 60,50 Z" fill="#5a6a4a" stroke="#c9a961" stroke-width="2"/>
        <path d="M 12,50 Q 20,38 28,42 Q 36,46 44,50 Z" fill="#6a7a5a" stroke="#c9a961" stroke-width="1"/>
        <circle cx="32" cy="30" r="4" fill="#8a6a5a" stroke="#c9a961" stroke-width="1.5"/>
        <line x1="32" y1="26" x2="32" y2="18" stroke="#6a4a3a" stroke-width="2"/>
        <polygon points="32,18 28,22 36,22" fill="#4a3a2a"/>
    </svg>''',
    
    'abbey': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
        <rect x="16" y="28" width="32" height="28" fill="#7a6a5a" stroke="#c9a961" stroke-width="2"/>
        <polygon points="32,10 16,24 48,24" fill="#8a7a6a" stroke="#c9a961" stroke-width="2"/>
        <rect x="28" y="4" width="8" height="20" fill="#6a5a4a" stroke="#c9a961" stroke-width="1.5"/>
        <rect x="30" y="2" width="4" height="4" fill="#c9a961"/>
        <rect x="24" y="38" width="8" height="10" fill="#4a3a2a" stroke="#c9a961" stroke-width="1"/>
        <rect x="34" y="38" width="8" height="10" fill="#4a3a2a" stroke="#c9a961" stroke-width="1"/>
        <circle cx="32" cy="30" r="3" fill="#ffd700"/>
        <line x1="18" y1="28" x2="18" y2="56" stroke="#c9a961" stroke-width="1"/>
        <line x1="46" y1="28" x2="46" y2="56" stroke="#c9a961" stroke-width="1"/>
    </svg>'''
}

# Create all icon files
for name, svg in icons.items():
    with open(f'/home/claude/location-icons/{name}.svg', 'w') as f:
        f.write(svg)

print(f"Created {len(icons)} icon files")
