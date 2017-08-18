import pprint
import MachineConfigs as machine_configs


# Get the html end.
def get_html_begin():
    return "<!DOCTYPE html> \n" +  " <html> \n"

# Get the html end.
def get_html_end():
    return "\n </html>"


def write_error_message_html(error_message):

    html_code = ""

    html_code = html_code + get_html_begin()

    html_code = html_code + "<body>"
    html_code = html_code + error_message
    html_code = html_code + "</body>"

    html_code = html_code + get_html_end()

    return html_code


def get_memory_check_table_html_code(tests_set_results):

    maxCols = 7
    memory_check_counts = 0
    memory_check_code = '<br>'
    memory_check_code += '<table style="width:100%" border="1">\n'
    memory_check_code += '<tr>\n'
    memory_check_code += '<th colspan=\'' + str(maxCols) + '\'> Memory Frame Checks </th> \n'
    memory_check_code += '</tr>\n'
    memory_check_code += '<th> Test </th> \n' + '<th> Start Time </th> \n' + '<th> End Time </th> \n' + '<th> Percent Difference </th> \n' + '<th> Start Frame Memory </th> \n' + '<th> End Frame Memory </th> \n' + '<th> Difference </th> \n'
    memory_error_code = ""






# Get the memory check table code.
def get_memory_check_table_code(tests_sets_results):

    maxCols = 7
    memory_check_counts = 0
    memory_check_code = '<br>'
    memory_check_code += '<table style="width:100%" border="1">\n'
    memory_check_code += '<tr>\n'
    memory_check_code += '<th colspan=\'' + str(maxCols) + '\'> Memory Frame Checks </th> \n'
    memory_check_code += '</tr>\n'
    memory_check_code += '<th> Test </th> \n' + '<th> Start Time </th> \n' + '<th> End Time </th> \n' + '<th> Percent Difference </th> \n' + '<th> Start Frame Memory </th> \n' + '<th> End Frame Memory </th> \n' + '<th> Difference </th> \n'
    memory_error_code = ""
    
    # For each test group.
    for current_test_group_name in tests_sets_results['Tests Groups']:
        current_test_group = tests_sets_results['Tests Groups'][current_test_group_name]

        if current_test_group['Enabled'] == 'True':
            if 'Results' in current_test_group:

                if 'Memory Time Checks' in current_test_group['Results']:
                        
                    current_group_memory_checks = current_test_group['Results']['Memory Time Checks']

                    for current_test_group_memory_checks_index in current_group_memory_checks:
                            
                        current_test_run_memory_checks = current_group_memory_checks[current_test_group_memory_checks_index]
                            
                        memory_check_code += '<tr>\n'
                        
                        for current_memory_time_check_index in current_test_run_memory_checks:
    
                            memory_check_code += '<td>' + current_test_group_name + '_' + str(current_test_group_memory_checks_index) + '</td>\n'

                            current_check = current_test_run_memory_checks[current_memory_time_check_index]

                            memory_check_counts = memory_check_counts + 1

                            memory_check_percent_change = float(current_check['Difference']) / float(current_check['SCCUVM'] )

                            comparison_threshold = machine_configs.machine_process_default_memory_percent_threshold

                            if 'Custom Memory Threshold'  in current_test_group:
                                comparison_threshold = current_test_group['Custom Memory Threshold']

                            if(abs(memory_check_percent_change) > comparison_threshold):
                                memory_check_code += '<font color="white"> ' + '<td bgcolor="red">' + str(current_check['Start Check Time']) + '</td>' + '<td bgcolor="red">' + str(current_check['End Check Time']) + '</td>' + '<td bgcolor="red">' + str(memory_check_percent_change) + '</td>' + '<td bgcolor="red">' + str(current_check['SCCUVM']) + '</td>' + '<td bgcolor="red">' + str(current_check['ECCUVM']) + '</td>' + '<td bgcolor="red">' + str(current_check['Difference']) + '</td>' + '</font> \n'
                                memory_error_code += '<p> Change in used memory exceeds threshold ' + machine_configs + ' for ' + current_test_group_name + '_' + str(current_test_group_memory_checks_index)  + '. <br> </p>'
                            else:
                                memory_check_code += '<font color="black"> ' + '<td bgcolor="white">' + str(current_check['Start Check Time']) + '</td>' + '<td bgcolor="white">' + str(current_check['End Check Time']) + '</td>' + '<td bgcolor="white">' + str(memory_check_percent_change) + '</td>' + '<td bgcolor="white">' + str(current_check['SCCUVM']) + '</td>' + '<td bgcolor="white">' + str(current_check['ECCUVM']) + '</td>' + '<td bgcolor="white">' + str(current_check['Difference']) + '</td>' + '</font> \n'

                            memory_check_code += '</tr>\n'
                            


    memory_check_code += '</table>\n'
    memory_check_code += '<br>'

    if memory_error_code != "" :
        memory_error_code = "<br> <p> Memory Check Errors : </p> \n " + memory_error_code + " \n <br>"

    if (memory_check_counts > 0.0):
        return [memory_check_code, memory_error_code]
    else :
        return ["", ""] 



def get_performance_check_table_code(tests_sets_results):
    return ["", ""]


# Get the image comparison table code.
def get_image_comparison_table_codex(screen_captures_results):

    max_image_comparison_counts = 0
    all_pass = True

    image_comparison_table_code = '<br>'
    image_comparison_table_code += '<table style="width:100%" border="1">\n'
    image_comparison_table_code += '<tr>\n'
    image_comparison_table_code += '<th colspan=\'' + str(max_image_comparison_counts + 1) + '\'>Image Compare Tests</th>\n'
    image_comparison_table_code += '</tr>\n'
    image_comparison_table_code += '<th>Test</th>\n'

    if screen_captures_results == 0 :
        retrn [True, ""]

    # For each test group.
    for current_test_run_screen_captures in screen_captures_results:
        
        if max_image_comparison_counts < len(current_test_run_screen_captures):
            max_image_comparison_counts = len(current_test_run_screen_captures)

    if max_image_comparison_counts == 0:
        return ["", ""]

    image_comparison_errors_code = ""
        
    for i in range (0, max_image_comparison_counts):
        image_comparison_table_code += '<th>SS' + str(i) + '</th>\n'

    for current_screen_capture_index in current_test_run_screen_captures:
        current_screen_capture = current_test_run_screen_captures[current_screen_capture_index]
        image_comparison_table_code += '<tr>\n'
        image_comparison_table_code += '<td>' + current_screen_capture['Title']  + '</td>\n'

        if current_screen_capture['Status']:
            image_comparison_table_code += '<td>' + str(current_screen_capture['Compare Result']) + '</td>\n'
        else :
            all_pass = False
            image_comparison_table_code += '<td bgcolor="red"><font color="white">' + str(current_screen_capture['Compare Result']) + '</font></td>\n'
    
    
    return [True, image_comparison_table_code]




# Get the image comparison table code.
def get_image_comparison_table_code(tests_sets_results):

    max_image_comparison_counts = 0

    # For each test group.
    for current_test_group_result_name in tests_sets_results['Tests Groups']:
        current_test_group = tests_sets_results['Tests Groups'][current_test_group_result_name]

        if current_test_group['Enabled'] == 'True':

            if 'Results' in current_test_group:

                if 'Screen Capture Checks' in current_test_group['Results']:
                    screen_captures_list = current_test_group['Results']['Screen Capture Checks']

                    for screen_captures_list_index in screen_captures_list:

                        if max_image_comparison_counts < len(screen_captures_list[screen_captures_list_index].keys()):
                            max_image_comparison_counts = len(screen_captures_list[screen_captures_list_index].keys())


    if max_image_comparison_counts == 0:
        return ["", ""]

    else:
        image_comparison_table_code = '<br>'
        image_comparison_table_code += '<table style="width:100%" border="1">\n'
        image_comparison_table_code += '<tr>\n'
        image_comparison_table_code += '<th colspan=\'' + str(max_image_comparison_counts + 1) + '\'>Image Compare Tests</th>\n'
        image_comparison_table_code += '</tr>\n'
        image_comparison_table_code += '<th>Test</th>\n'

        image_comparison_errors_code = ""
        
        for i in range (0, max_image_comparison_counts):
            image_comparison_table_code += '<th>SS' + str(i) + '</th>\n'
        
        for current_test_group_result_name in tests_sets_results['Tests Groups']:
            current_test_group = tests_sets_results['Tests Groups'][current_test_group_result_name]

            # Check if the current test group is enabled.
            if current_test_group['Enabled'] == 'True':

                if 'Results' in current_test_group:

                    #     
                    if 'Screen Capture Checks' in current_test_group['Results']:
                        screen_captures_list = current_test_group['Results']['Screen Capture Checks']
    
                        for screen_captures_list_index in screen_captures_list:
                            
                            # Construct the list of captures.
                            if len(screen_captures_list[screen_captures_list_index].keys()) > 0:
                                image_comparison_table_code += '<tr>\n'
                                image_comparison_table_code += '<td>' + current_test_group_result_name + '_' + str(screen_captures_list_index) + '</td>\n'

                                # 
                                for screen_capture_checks_index in screen_captures_list[screen_captures_list_index]:
                                    screen_capture_compare_result = screen_captures_list[screen_captures_list_index][screen_capture_checks_index] 
                                    result_value_str = screen_capture_compare_result["Compare Result"]

                                    # Check if this was a comparison.
                                    try:
                                        result_value = float(result_value_str)

                                        comparison_threshold = machine_configs.machine_process_default_image_threshold

                                        if 'Custom Image Threshold' in current_test_group:
                                            comparison_threshold = current_test_group['Custom Image Threshold']
                                        

                                        if float(result_value) > comparison_threshold:
                                            image_comparison_table_code += '<td bgcolor="red"><font color="white">' + str(result_value) + '</font></td>\n'
                                        else:
                                            image_comparison_table_code += '<td>' + str(result_value) + '</td>\n'
                                        
                                    except:
                                        image_comparison_errors_code = "<p> " + image_comparison_errors_code + "" + current_test_group_result_name + '_' + str(screen_captures_list_index) + " failed to compare screen capture " + str(screen_capture_checks_index) + " <br> \n"
                                        image_comparison_errors_code = image_comparison_errors_code + "Source : " + screen_capture_compare_result["Source Filename"] + " <br>  Reference : " + screen_capture_compare_result["Reference Filename"] + " <br> \n"
                                        image_comparison_errors_code = image_comparison_errors_code + "Please check whether the images are output correctly, whether the reference exists and whether they are the same size. <br> "
                                        image_comparison_errors_code = image_comparison_errors_code + "Actually, just do the references manually. <br> </p>"
                                        image_comparison_table_code += '<td bgcolor="red"><font color="white">' + str(-1) + '</font></td>\n'
                                        continue
                            

                                image_comparison_table_code += '</tr>\n'


        image_comparison_table_code += '</table>\n'
        image_comparison_table_code += '<br>'
        return [image_comparison_table_code, image_comparison_errors_code]        




# Write the provided Tests Set Results to HTML and Return them.
def write_test_set_results_to_html(tests_set_results):
    
    html_code = ""

    html_code = html_code + get_html_begin()

    html_code = html_code + "<body>"
    if tests_set_results['Tests Set Error Status'] is True:
        html_code = html_code + '<p>' + tests_set_results['Tests Set Error Message'] + '</p>'
    else:
        image_comparisons = get_image_comparison_table_code(tests_set_results)
        html_code = html_code + image_comparisons[0]
        html_code = html_code + '\n <hr> \n'

        memory_comparison = get_memory_check_table_code(tests_set_results)
        html_code = html_code + memory_comparison[0]
        html_code = html_code + '\n <hr> \n'
        

        if image_comparisons[1] != "" or memory_comparison[1] != "":
            html_code = html_code + '\n <hr> \n'
            html_code = html_code + image_comparisons[1]
            html_code = html_code + memory_comparison[1]

    html_code = html_code + "</body>"

    html_code = html_code + get_html_end()
    return html_code