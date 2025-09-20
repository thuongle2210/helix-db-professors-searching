// Start building your schema here.
//
// The schema is used to to ensure a level of type safety in your queries.
//
// The schema is made up of Node types, denoted by N::,
// and Edge types, denoted by E::
//
// Under the Node types you can define fields that
// will be stored in the database.
//
// Under the Edge types you can define what type of node
// the edge will connect to and from, and also the
// properties that you want to store on the edge.
//
// Example:
//
// N::User {
//     Name: String,
//     Label: String,
//     Age: Integer,
//     IsAdmin: Boolean,
// }
//
// E::Knows {
//     From: User,
//     To: User,
//     Properties: {
//         Since: Integer,
//     }
// }
//
// For more information on how to write queries,
// see the documentation at https://docs.helix-db.com
// or checkout our GitHub at https://github.com/HelixDB/helix-db


// NODES //

N::Professor {
    name: String,
    title: String,
    page: String,
    bio: String,
}

N::ResearchArea {
    research_area: String,
    description: String,
}

N::Department {
    name: String,
}   

N::University {
    name: String,
}

N::Lab {
    name: String,
    research_focus: String,
}


// Connect Professor to Lab
E::HasLab {
    From: Professor,
    To: Lab,
}

// Connect Professor to Research Area
E::HasResearchArea {
    From: Professor,
    To: ResearchArea,
}

// EDGES //

// Connect Professor to University
E::HasUniversity {
    From: Professor,
    To: University,
    Properties: {
        since: Date DEFAULT NOW,
    }
}

// Connect Professor to Department
E::HasDepartment {
    From: Professor,
    To: Department,
    Properties: {
        since: Date DEFAULT NOW,
    }
}

// VECTORS //

// Connect Professor to Research Area + Description
V::ResearchAreaAndDescriptionEmbedding {
    areas_and_descriptions: String,
}

E::HasResearchAreaAndDescriptionEmbedding {
    From: Professor,
    To: ResearchAreaAndDescriptionEmbedding,
    Properties: {
        areas_and_descriptions: String,
    }
}