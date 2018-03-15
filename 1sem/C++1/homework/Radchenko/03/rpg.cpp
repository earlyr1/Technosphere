#include <vector>

enum Slot {HEAD, LEFTHAND, RIGHTHAND, TORSO};
enum {N_SLOTS = 4, BCKPK_SZ = 10};

using std::vector;

class Thing {
public:
	int HP;
	int max_hp;
	Thing(int hp) {
		HP = hp;
		max_hp = hp;
	}
	virtual ~Thing() {;}
};

class Weapon: public Thing {
public:
	int attack;
	int defense;
	Slot slot;
	void Hit() {;}

	Weapon(int atk, int dfs, int HP, Slot slt): Thing(HP) {
		attack = atk;
		defense = dfs;
		slot = slt;
	}
	virtual ~Weapon() {;}
};

class MeleeWeapon: public Weapon {
public:
	MeleeWeapon(int atk, int dfs, int HP, Slot slot): Weapon(atk, dfs, HP, slot) {;}
	virtual ~MeleeWeapon() {;}
};

class Sword: public MeleeWeapon {
public:
	Sword(int atk, int dfs, int HP): MeleeWeapon(atk, dfs, HP, RIGHTHAND) {;}
	~Sword() {;}
};

class Knife: public MeleeWeapon {
public:
	Knife(int atk, int dfs, int HP): MeleeWeapon(atk, dfs, HP, LEFTHAND) {;}
};

class RangeWeapon: public Weapon {
public:
	int range;
	RangeWeapon(int atk, int dfs, int HP, int rng, Slot slot): Weapon(atk, dfs, HP, slot) {
		range = rng;
	}
	virtual ~RangeWeapon() {;}
};

class Bow: public RangeWeapon {
public:
	Bow(int atk, int dfs, int HP, int rng, Slot slot): RangeWeapon(atk, dfs, HP, rng, slot) {;}
	~Bow() {;}

};

class Armor: public Weapon {
public:
	Armor(int atk, int dfs, int HP, Slot slot): Weapon(atk, dfs, HP, slot) {;}
	virtual ~Armor() {;}
};

class Vest: public Armor {
public:
	Vest(int atk, int dfs, int HP): Armor(atk, dfs, HP, TORSO) {;}
	~Vest() {;}
};

class Tool: public Thing {
public:
	Slot slot;
	Tool(int HP, Slot slt): Thing(HP) {
		slot = slt;
	}
	virtual ~Tool() {;}
};

class Shovel: public Tool {
public:
	Shovel(): Tool(HP, RIGHTHAND) {;}
	~Shovel() {;}
	void Dig() {;}
};

class Container {
public:
	int size;
	vector<Thing> things;
	int n;
	Container(int sz) {
		things = vector<Thing>(sz, Thing(-1));
		n = 0;
		size = sz;
	}
	Thing& operator [](int i) {
		if (i < n) return things[i]; 
		else throw -1;
	}
	virtual ~Container() {;}
};

class Arsenal: public Container {
public:
	Arsenal(): Container(N_SLOTS) {;}
	~Arsenal() {;}
};

class Backpack: public Container {
public:
	Backpack(): Container(BCKPK_SZ) {;}
	~Backpack() {;}
};


class Alive {
public:
	int HP;
	bool alive;
	void Move() {if (~alive) return;}
	Alive(int hp) {
		HP = hp;
		alive = true;
	} 
	virtual ~Alive() {;}
};

class Animal: public Alive {
public:
	Animal(int HP): Alive(HP) {;}
	virtual ~Animal() {;}
};


class Swine: public Animal {
public:
	Swine(): Animal(20) {;}
	~Swine() {;}
};


class Human: public Alive {
public:
	Arsenal arsenal;
	Backpack backpack;
	int attack, defense, level;
	void Attack() {;}
	void TakeThing() {;}
	void DropThing() {;}
	void TakeOnThing() {;}
	void TakeOffThing() {;}
	void LevelUp() {;}
	Human(): Alive(100) {
		arsenal = Arsenal();
		backpack = Backpack();
		attack = 0;
		defense = 0;
		level = 1;
	}
	virtual ~Human() {;}
};


class Knight: public Human {
public:
	Knight(): Human() {
		attack = 0; defense = 1;
	}
	~Knight() {;}
};

class Archer: public Human {
public:
	Archer(): Human() {
		attack = 1; defense = 0;
	}
	~Archer() {;}
};

class Farmer: public Human {
public:
	Farmer(): Human() {
		arsenal[0] = Shovel();
	}
	~Farmer() {;}
};


int main() {;}