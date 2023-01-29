function createStates(jsonInput) {
    // given some json input, return a big dict of all states for micro
    output = {}
    for (const func in jsonInput) {
      output[func] = {}
      for (const variable in jsonInput[func]) {
        output[func][variable] = {}
        if (jsonInput[func][variable]["type"] === "list") {
          for (const invocation in jsonInput[func][variable]["invocations"]) {
            // Set the initial state in the state list
            output[func][variable][invocation] = [];
            output[func][variable][invocation][0] = jsonInput[func][variable]["invocations"][invocation]["initial"];
            // Go through each operation
            for (var i = 0; i < jsonInput[func][variable]["invocations"][invocation]["operations"].length; i++) {
              var length = output[func][variable][invocation].length;
              var operation = jsonInput[func][variable]["invocations"][invocation]["operations"][i];
              if (operation[0] === "append") {
                // Set the new state to the previous state, with the new element concatenated
                output[func][variable][invocation][length] = output[func][variable][invocation][length-1].concat(operation[1][0]);
              } else if (operation[0] === "__delitem__") {
                // Set the new state to a shallow copy of the previous state, and splice the removed index
                output[func][variable][invocation][length] = [...output[func][variable][invocation][length-1]];
                output[func][variable][invocation][length].splice(operation[1][0], 1);
              } else {
                return error;
              }
            }
          }
        } else {
          return error;
        }
      }
    }
    return output;
}