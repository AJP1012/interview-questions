#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <memory>

using namespace std;

struct unitNode {

    string unit;
    vector<pair<float, weak_ptr<unitNode>>> neighbourhood;

    unitNode(string unit) : unit(unit) {};
    
};

class unitGraph {

    private:
        unordered_map<string, shared_ptr<unitNode>> graph;

    public:
        unitGraph() {};
        shared_ptr<unitNode> get(string unit) {}
        bool exists(string unit) {return graph.find(unit) != graph.end();} 
        void addConversion(float conversion, shared_ptr<unitNode> from, shared_ptr<unitNode> to);

};

void unitGraph::addConversion(float conversion, shared_ptr<unitNode> from, shared_ptr<unitNode> to) {

    if (conversion == 0) return;

    weak_ptr<unitNode> weakfrom = from;
    weak_ptr<unitNode> weakto = to;

    from->neighbourhood.emplace_back(conversion, weakto); 
    to->neighbourhood.emplace_back(1 / conversion, weakfrom);

}

float convert(string fromUnit, string toUnit, unitGraph& units) {

    if (!units.exists(fromUnit)) throw invalid_argument("Unit " + fromUnit + " is undefined.");
    if (!units.exists(toUnit)) throw invalid_argument("Unit " + toUnit + " is undefined.");

    shared_ptr<unitNode> fromUnit = 

}


