function createStates(jsonInput) {
    // given some json input, return a big dict of all states for micro
    output = {}
    for (const func in jsonInput) {
      output[func] = {}
      for (var vCount = 0; vCount < jsonInput[func].length; vCount++) {
        var variableName = jsonInput[func][vCount].name;
        output[func][variableName] = []
        if (jsonInput[func][vCount]["type"] === "list") {
          for (var invocation = 0; invocation < jsonInput[func][vCount]["invocations"].length; invocation++) {
            if (jsonInput[func][vCount]["invocations"][invocation] != null) {
              // Set the initial state in the state list
              output[func][variableName][invocation] = [];
              output[func][variableName][invocation][0] = jsonInput[func][vCount]["invocations"][invocation]["initial_value"];
              // Go through each operation
              for (var i = 0; i < jsonInput[func][vCount]["invocations"][invocation]["operations"].length; i++) {
                var length = output[func][variableName][invocation].length;
                var operation = jsonInput[func][vCount]["invocations"][invocation]["operations"][i];
                if (operation[0] === "append") {
                  // Set the new state to the previous state, with the new element concatenated
                  output[func][variableName][invocation][length] = output[func][variableName][invocation][length-1].concat(operation[1][0]);
                } else if (operation[0] === "__delitem__") {
                  // Set the new state to a shallow copy of the previous state, and splice the removed index
                  output[func][variableName][invocation][length] = [...output[func][variableName][invocation][length-1]];
                  output[func][variableName][invocation][length].splice(operation[1][0], 1);
                } else {
                  return error;
                }
              }
            }
          }
        } else if (jsonInput[func][vCount]["type"] === "dict") {
          for (var invocation = 0; invocation < jsonInput[func][vCount]["invocations"].length; invocation++) {
            if (jsonInput[func][vCount]["invocations"][invocation] != null) {
              // Set the initial state in the state list
              output[func][variableName][invocation] = [];
              output[func][variableName][invocation][0] = jsonInput[func][vCount]["invocations"][invocation]["initial_value"];
              // Go through each operation
              for (var i = 0; i < jsonInput[func][vCount]["invocations"][invocation]["operations"].length; i++) {
                var length = output[func][variableName][invocation].length;
                var operation = jsonInput[func][vCount]["invocations"][invocation]["operations"][i];
                if (operation[0] === "__setitem__") {
                  // Set the new state to the previous state, with the new element concatenated
                  output[func][variableName][invocation][length] = {...output[func][variableName][invocation][length-1]};
                  output[func][variableName][invocation][length][operation[1][0]] = jsonInput[func][vCount]["invocations"][invocation]["operations"][i][1][1];
                } else if (operation[0] === "__delitem__") {
                  // Set the new state to a shallow copy of the previous state, and splice the removed index
                  output[func][variableName][invocation][length] = {...output[func][variableName][invocation][length-1]};
                  delete output[func][variableName][invocation][length][output[1][0]];
                } else {
                  return error;
                }
              }
            }
          }
        }
      }
    }
    console.log(output);
    return output;
}

module.exports = createStates;