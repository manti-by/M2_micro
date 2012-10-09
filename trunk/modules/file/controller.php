<?php
    defined('M2_MICRO') or die('Direct Access to this location is not allowed.');

    /**
     * File Controller class
     * @name $fileController
     * @package M2 Micro Framework
     * @subpackage Modules
     * @author Alexander Chaika
     * @since 0.3RC2
     */
    class FileController extends Controller {

        public function indexAction($options) {
            // Get frontpage contents items
            $options['title'] = 'Default file list of M2 Micro Framework';
            $options['body']  = '<h1>File page of M2 Micro Framework</h1>';

            return $options;
        }
    }
