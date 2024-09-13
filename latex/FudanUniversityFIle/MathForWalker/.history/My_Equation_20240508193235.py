import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


g = 9.81
l = 1
gamma = 0.02
beta = 0.005

theta_0 = 0.2
theta_dot_0 = 0
phi_0 = 0.4
phi_dot_0 = 0

variable_list_0 = [theta_0, theta_dot_0, phi_0, phi_dot_0]


def equations(t, variable_list):

    theta, theta_dot, phi, phi_dot = variable_list

    matrix_A = np.array([[1+2*beta*(1-np.cos(phi)), -beta*(1-np.cos(phi))],
                         [beta*(1-np.cos(phi)),     -beta                ]])
    
    vector_B = np.array([-beta*np.sin(phi)*(phi_dot**2-2*theta_dot*phi_dot),
                         beta*theta_dot**2*np.sin(phi)                     ])
                         
    vector_C = np.array([beta*g/l*(np.sin(theta-phi-gamma)-np.sin(theta-gamma)-g/l*np.sin(theta-gamma)),
                         beta*g/l*np.sin(theta-phi-gamma)])

    theta_ddot, phi_ddot = np.linalg.solve(matrix_A, -vector_B-vector_C)
    
    return [theta_dot, theta_ddot, phi_dot, phi_ddot]


def heelstrike_event_and_change_defination(variable_list):

     theta, theta_dot, phi, phi_dot = variable_list

     matrix_Change = np.array([[-1, 0,                                   0, 0],
                               [0,  np.cos(2*theta),                     0, 0],
                               [-2,  0,                                  0, 0],
                               [0,  np.cos(2*theta)*(1-np.cos(2*theta)), 0, 0]])
     
     variable_matrix = np.array([[theta],
                                 [theta_dot],
                                 [phi],
                                 [phi_dot]])    

     result_matrix = np.dot(matrix_Change, variable_matrix)

     theta_new = result_matrix[0, 0]
     theta_dot_new = result_matrix[1, 0]
     phi_new = result_matrix[2, 0]
     phi_dot_new = result_matrix[3, 0]

     return [theta_new, theta_dot_new, phi_new, phi_dot_new]


def monitor(t, variable_list):

    theta, theta_dot, phi, phi_dot = variable_list

    return phi - 2*theta


