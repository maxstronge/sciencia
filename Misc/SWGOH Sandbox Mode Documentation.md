
***

**Project Directory:**

These are all folders - bold are important folders - italics are not folders but just lists of the specific items inside a folder, organized by type

- SWGOH_Sandbox
	- Assets (looks to be mostly default content)
		- Audio
		- Level
		- Materials
		- Models
		- Widgets
	- **Blueprints**
		- FunctionLibrary
			- *Function Library:*
				- BP_FL_General
				- BP_FL_Combat
		- GameInstance (contains game instance blueprint BP_GI)
		- **GameModes**
			- Base (template GM/GS/PS/PC)
			- **Combat**
				- **Abilities** (contains a folder for each character with ability blueprints)
					- *Blueprints:*
						- BaseCombatAbility (all subtypes inherit from this)
							- BasicAbility
							- SpecialAbility
							- LeadershipAbility
							- UniqueAbility
							- GrantedAbility
							- UltimateAbility
					- *Function Library:*
						- BPL_Abilities (does not follow naming convention, should probably be consolidated into BP_FL_Combat)
					- *Interface:*
						- BPI_CombatAbility (interface to execute abilities of all types)
				- **Core** (GameMode and GameState for combat)
				- **Player** (BP_Combat_Camera, BP_HUD_Combat, player controller/state for combat, blueprint component for click trace interaction, enum team filter for enemy/ally/both)
				- **StatusEffects** 
					- Blue (contains BP for each blue status inheriting from BP_StatusEffect below)
					- Buffs (contains BP for each buff)
					- Debuffs (contains BP for each debuff)
					- *Blueprints:*
						- BP_StatusEffect (core BP for status effect logic)
					- *Interface:*
						- BPI_Status (interface to apply/expire status effects)
				- **Unit**
					- *Blueprints:*
						- BP_Unit (core BP for unit in combat - very important)
					- SelectionRing (contains blueprints, material instances for different types of selection ring)
			- Lobby (blueprints for Lobby GameMode, GameState, PlayerState, PlayerController, HUD)
			- MainMenu (GameMode and PlayerController for main menu)
		- Interfaces (Interaction/UI interfaces from template)
		- MacroLibrary (macro libraries to get/validate player states/controllers/game modes/states)
		- **SaveGame** (data for saved player profiles (mod library, avatar, player name, team presets), saved game settings like audio etc)
		- Systems
			- Chat (in-game chat during lobby and battle)
			- Log (battle log, event history/order of operation)
	- **Characters** (assets for character models/blueprints)
		- \_Anims
			- Lightsaber (sword animation pack)
			- Shared (hit/death)
		- \_Core
			- Blueprints (contains base character blueprint only)
			- Materials (base character material and 'T_White_Masks' - what does this do?)
			- Meshes (skeletal meshes, skeleton, control rig, IK retargeter, physics asset)
			- Textures ('T_Char_Base_BC' - just CLS base texture)
		- \_Weapons
			- \_Core
				- LightsaberMats (materials, curve atlas, color curves, textures for lightsabers)
			- \_FX (sparkle burst, looks like on hit effect?)
			- Lightsabers (specific lightsaber blueprints/hilt meshes/material instances)
			- Blasters (same, meshes/blueprints/materials)
			- Rifles (same)
		- *Character Folders* (one for each char, contains a skeletal mesh, texture/mask, material instance, character blueprint, animBP)
	- **Data**
		- DataTables (contains DT for: status effects, levels, character models, abilities, ability descriptions)
			- CharacterStats (one DT each for G13 thru R9, containing stats for all characters)
		- Enums (enums for arrow/ring brush color, background levels, stats, tags, battle type, battle mode)
		- Structs (ability description, character blueprint map, level background, source char stats)
	- **Environments**
		- Shared (light controller)
		- Bridge (level, built data, alpha curve, thumbnail)
			- Mats
			- Meshes
			- Textures
	- **Maps** (should maybe rename this to 'Levels')
		- Boot Level (not currently in use I don't think)
		- Main Menu Level
		- Transition Level
		- Lobby Level (needs game flow rework but looks great)
		- Combat Level
	- **UI_Content**
		- Fonts (all fonts used in project)
		- Mats
			- AbilitySlot (materials for the anchor timer, cooldown overlay)
			- Borders (curve atlas, gradient/grad ramp, border materials)
			- Button (sound effects+cues, button materials/material instances)
			- CharacterSlot (material instances for roster screen character slot backgrounds)
			- StatusEffects
				- Background (background/trim materials for status effect icons)
				- StatusIcons (material instances for status effect icons)
		- Structs (has data table for rich text ability descriptions (i.e. stylers for debuff, buff, omicron, etc), struct for button materials)
		- Textures (also contains texture and material for the imperial bridge floor, as well as studio HDRI)
			- Borders (one blue border texture)
			- Button (textures for buttons/plus sign)
			- Icons (cogwheel, selection ring, statuseffect icon map, lock icon)
			- VFX (only one random NewNiagaraSystem)
	- **Widgets** (most combat widgets are here)
		- BootScreen (wb for boot screen)
		- **Combat** 
			- Arrows (widgets for active/target unit - deprecated)
			- UnitWidgets (deprecated old 2D unit widgets)
			- *Widget Blueprints:*
				- CombatTimer
				- HUD_Combat
				- deprecated unit widget
				- CombatHeader
				- CombatAbilityButton
				- CombatAbilityDescription
				- CombatLog
				- CombatStatRow
				- CurrentUnitInfo
				- HighlightedUnitInfo
				- StatusEffect
				- StatusEffectTray
				- TurnOrder
				- UnitSlot
		- Encyclopedia (4 structs for different unnamed categories, widgets for EncyclopediaMenu, EncyclopediaPage, EncyclopediaTopicButton)
			- GeneralPages (contains enc page called TM, unfinished)
		- Gameplay
			- AuthorityIndicator (widget for host/client)
			- GameMenu (wb for game menu / settings)
			- **Lobby** 
				- Controls (control hints, from multiplayer lobby template)
				- Ready Indicator (ready status widget)
				- ReadyUpIndicator (readyup indicator)
				- Updated (character slot temp)
				- *Widget Blueprints*:
					- HUD_Lobby
					- AbilitySlot
					- AbilityTray
					- BattleDetails
					- CharacterRosterGrid
					- LobbyCharacterSlot
					- Lobby_Header
					- SquadSelection
					- StatEdit
					- Stats_Row_Edit
					- TagList
					- TeamPreview
					- TeamSetup
					- Unit_Details_Gear_Lvl
					- Unit_Details_Stats
			- PlayerList (from multiplayer lobby template)
			- PlayerName (from multiplayer lobby template)
		- **General**
			- Widget Blueprints:
				- Loading Screen
				- BaseOptionSwitcher (template)
				- WB_Marketplace_Promo (template)
				- PopUp (template)
				- BaseButton
				- Border_A
				- Make_Changes
				- Tag_Button
		- MainMenu
			- Widget Blueprints:
				- Main Menu
				- Server_List_Item (template)
		- Profile (contains WB for profile creator and struct for profile avatar)


***
# Main Menu:

- Level: MainMenu_Level
- GameMode: BP_GM_MainMenu
- Player Controller: BP_PC_MainMenu

## Events:
### **BeginPlay:**
- the GameMode **BP_GM_MainMenu** gets a reference to / validates the GameInstance **BP_GI**.
- The Player Controller **BP_PC_MainMenu** does the following things in order:
	- 1. validates that it IsLocalPlayerController (should always be, might be unnecessary)
	- 2. uses Does Save Game Exist for slotname UserProfile to check if the player has a saved profile - if yes, call the custom event CreateMainMenu to initialize the menu, if no, go to 3.
	- 3. sets up the Profile Creation by creating the WB_Profile_Creation widget/adding it to the viewport, and then binding the 'make changes' button to the CreateMainMenu event

### **CreateMainMenu:**
- After a brief delay, use Load Game From Slot to load the UserProfile, cast it to the BP_SG_PlayerProfile blueprint, and store a reference to it called 'Profile SaveGame'
- Then, create the MainMenu widget WB_MainMenu, add it to the viewport and set input mode UI only

## WB_MainMenu:
![[Pasted image 20231111163024.png]]

Main widget class for the Main Menu. Need to rework a fair bit to accommodate GAC mode vs single battle (instead of just Host Game/Join Game). 

**Buttons:**
- Host Game -> Set Settings (max players, connection type LAN vs online) -> Host
- Join Game -> Choose Server from available -> Join

	When the Host button is selected, the widget casts the local player controller to BP_PC_MainMenu and then uses the Create Session node (with the parameters selected, connection type / max players). On success, a loading screen is created (this is achieved using a function library function), a short delay is triggered, and then the Open Level (by name) node is used to open the Lobby_Level with options='listen' to create a listen server.


****


# Lobby:

- Level: Lobby_Level
- GameMode: BP_GM_Lobby
- Game State: BP_GS_Lobby
- Player Controller: BP_PC_Lobby


### **BeginPlay**:

- GameMode:
	- Use Switch Has Authority to ensure this only happens on the server
	- Validate / get reference to the GameInstance and GameState
- PlayerController:
	- Validate / get reference to PlayerState
	- validates that it IsLocalPlayerController - all execution from here on out assumes yes
	- Create the lobby HUD widget WB_HUD_Lobby, get reference to it, set input mode game and ui and add to viewport
	- Validate/Get references to the GameState and GameInstance
	- use Does Save Game Exist to check for slot name TestProfileSaveSlot
		- If save game data is found, load it from slot and store a reference to it called PlayerProfileRef
		- If not found, use the Create Save Game Object node to create a player profile object, set it with default parameters, and Save Game to Slot
	- Set up the chat widget
	- Use the SwitchHasAuthority node:
		- If host, set the HostPlayerController variable in the GameState with value of Self
		- If client, do the same for ClientPlayerController variable in GameState
- PlayerState:
	- Validate/get reference to GameState
- GameState:
	- Execute the parent BeginPlay (inherits from GameState Base)
	- Use SwitchHasAuthority to ensure all that follows happens on the host
	- Validate/get reference to GameInstance and GameMode

## WB_Lobby
![[Pasted image 20231112172524.png]]





____




# Combat:


# Player Controller: 

In the replicated multiplayer version of combat, a lot of stuff had to be done through the local player controller and replicated to the server, so any visual update to the UI needed to be handled through the PC for replication purposes. This can safely be avoided if we're only going to have one player viewing a battle

## Events:

- **BeginPlay:**
	- Store a reference to self in the Tracer Component
	- Ensure IsLocalPlayerController (deprecate for single-player combat mode)
	- Create HUD widget, store reference to it, Set Input Mode Game and UI, Add to Viewport
	- Setup Log Widget / store reference
	- Switch on is Host/is Client (this will no longer be necessary for SP)
		- Based on the above switch, initialize camera with the appropriate transform, set view target

- **Initialize Characters**
	- Input parameter: 
		- AllUnits (array of all characters in combat)
	- Loops through all these characters and calls *InitializeCharacter* function of each one

- **Client_StartUnitTurn**
	- Input parameter: 
		- ActiveUnit (BP_Unit), the unit to start the turn with
	- Check IsLocalPlayerController
	- Validate the unit (pure func)
	- If validated, set this Player Controller's ActiveUnit variable to ActiveUnit input parameter
	- Call **Server_TurnStart** on the unit (event in BP_Unit) - this was being called on the server so both players could see the active unit indicator light up underneath the unit
	- Change the Current Unit on the WB_HUD with *UpdateCurrentUnit* func
	- Call *ChangeCurrentUnitVisibility* func on WB_HUD, set Visible? to true 
	- Set the autotarget (unimplemented, todo)

- **Server_EndUnitTurn**
	- Checks that the current Active Unit of the PC has the IsMyTurn? flag to True
		- If yes, call **Multicast_TurnEnd** event of that unit (multicast to turn the active ring off, unnecessary now)
		- Call PlayerTurnOver event dispatcher

- **Client_UpdateTurnOrderWidget**
	- Input parameter:
		- TurnQueue (Array of BP_Units) sorted array in turn order
	- Get WBC_TurnOrderGraph ref from WB_HUD ref and call *UpdateTurnOrderGraph* function

- **Client_HideCurrentUnit**
	- Call **Client_ChangeCurrentUnitVisibility** event on WB_HUD ref, Visible? set to false

- **Client_UpdateTargetedUnit**
	- Input parameter:
		- SelectedUnit (BP_Unit)
	- Check if the variable TargetedUnit is already a valid unit:
		- Yes: Is the SelectedUnit already the targeted unit?
			- Yes: break
			- No: Call **ToggleSelectionRing** event on targeted unit to turn red ring off, call **ToggleSelectionRing** selected unit to turn red ring on, set the TargetedUnit reference to the SelectedUnit, and call *UpdateTargetUnit* func in the WB_HUD 
		- No:
			- call **ToggleSelectionRing** on selected unit to turn red ring on, set the TargetedUnit reference to the SelectedUnit, and call *UpdateTargetUnit* func in the WB_HUD 

- **Server_ActivateAbility**
	- Input parameters:
		- Unit (BP_Unit)
		- Target (BP_Unit)
		- Ability (BaseCombatAbility)
	- Set TM variable of Unit to 0.0
	- Call **Client_HideCurrentUnit** (self)
	- Call *ExecuteAbility* (BPI_CombatAbility, overridden by Ability input param) - returns a boolean if the ability executed or not
		- Executed: 
			- Bind custom event **Server_EndUnitTurn** (self) to event dispatcher AbilityFinishedExecution
			- Get variable AbilityTime (float) from AbilityBP, and delay for that time
			- Call AbilityFinishedExecution
		- Not Executed:
			- Print debug string and manually call **Server_EndUnitTurn**

- **Server_StatusTest**
	- Test event to check application of status effects (deprecated)


- **Server_ApplyStatusEffect**
	- Input parameters:
		- Applying Unit (BP_Unit)
		- Receiving Unit (BP_Unit)
		- Chance to Apply (float)
		- Status Effect (StatusNameEnum)
		- Duration (int)
		- Resistable? (bool)
		- Dispellable? (bool)
	- Calls *CalculateDebuffProc?* function from BP_FL_Combat (this shouldn't happen for a buff) - returns Proc? bool
	- If Proc? yes, call **Server_GainStatusEffect** event on receiving Unit (this creates the status actor, handles creation/updating of the icon, and application logic)

## Functions:

-


***


# BP_Unit

